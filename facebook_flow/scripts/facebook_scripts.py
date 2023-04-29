import pandas as pd
import requests
import json

def getCampaignData(account_id, access_token, since, until):
        campaigns = pd.DataFrame()
       
        fields = "campaign_name,campaign_id,adset_name,adset_id,ad_name,ad_id,clicks,reach,impressions,objective,spend,actions, action_values"

        url = f"https://graph.facebook.com/v16.0/{account_id}/insights?level=ad&fields={fields}&access_token={access_token}&time_range[since]={since}&time_range[until]={until}"

        payload = {}
        headers = {
        '': ''
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        data = json.loads(response.content)

        flat_data = []

        for record in data:

            actions_dict = {}
            try:
                for action in record['actions']:
                    actions_dict[f"actions.{action['action_type']}"] = action['value']
            except Exception as e:
                pass
                    
            action_values_dict = {}
            try:
                for action_value in record['action_values']:
                    action_values_dict[f"action_values.{action_value['action_type']}"] = action_value['value']
            except Exception as e:
                pass

            conversions = [
                    'actions.omni_initiated_checkout', 'actions.omni_add_to_cart', 'actions.omni_purchase', 
                    'actions.post_engagement', 'actions.video_view', 'actions.link_click', 'actions.lead'
                ]

            filtered_actions = {k: v for k, v in actions_dict.items() if k in conversions}

            conversions_value = [
                    'action_values.omni_purchase'
                ]

            filtered_action_value = {k: v for k, v in action_values_dict.items() if k in conversions_value}

            flat_record = {
                'campaign_name': record['campaign_name'],
                'campaign_id': record['campaign_id'],
                'adset_name': record['adset_name'],
                'adset_id': record['adset_id'],
                'ad_name': record['ad_name'],
                'ad_id': record['ad_id'],
                'clicks': record['clicks'],
                'reach': record['reach'],
                'impressions': record['impressions'],
                'objective': record['objective'],
                'spend': record['spend'],
                **filtered_actions,
                **filtered_action_value,
                'date_start': record['date_start'],
                'date_stop': record['date_stop'],
            }
            flat_data.append(flat_record)

        campaigns = pd.DataFrame(flat_data)
        campaigns['account'] = account_id
        
        return campaigns