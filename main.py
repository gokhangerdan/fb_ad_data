from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
import json


class LibFacebook:
    def __init__(self, app_id, app_secret, access_token, ad_account_id):
        FacebookAdsApi.init(app_id, app_secret, access_token)
        self.account = AdAccount(ad_account_id)

    def create_ad_tree(self):
        # Campaign fields
        fields = ["id",
                  "account_id",
                  "adlabels",
                  "bid_strategy",
                  "boosted_object_id",
                  "brand_lift_studies",
                  "budget_rebalance_flag",
                  "budget_remaining",
                  "buying_type",
                  "can_create_brand_lift_study",
                  "can_use_spend_cap",
                  "configured_status",
                  "created_time",
                  "daily_budget",
                  "effective_status",
                  "issues_info",
                  "lifetime_budget",
                  "name",
                  "objective",
                  "recommendations",
                  "source_campaign",
                  "source_campaign_id",
                  "spend_cap",
                  "start_time",
                  "status",
                  "stop_time",
                  "updated_time"]

        # List of all campaigns
        campaigns = self.account.get_campaigns(fields=fields)

        # Ad set fields
        fields = ["id",
                  "account_id",
                  "adlabels",
                  "adset_schedule",
                  "attribution_spec",
                  "bid_amount",
                  "bid_info",
                  "bid_strategy",
                  "billing_event",
                  "budget_remaining",
                  "campaign",
                  "campaign_id",
                  "configured_status",
                  "created_time",
                  "creative_sequence",
                  "daily_budget",
                  "daily_min_spend_target",
                  "daily_spend_cap",
                  "destination_type",
                  "effective_status",
                  "end_time",
                  "frequency_control_specs",
                  "instagram_actor_id",
                  "is_dynamic_creative",
                  "issues_info",
                  "lifetime_budget",
                  "lifetime_imps",
                  "lifetime_min_spend_target",
                  "lifetime_spend_cap",
                  "name",
                  "optimization_goal",
                  "pacing_type",
                  "promoted_object",
                  "recommendations",
                  "recurring_budget_semantics",
                  "rf_prediction_id",
                  "source_adset",
                  "source_adset_id",
                  "start_time",
                  "status",
                  "targeting",
                  "time_based_ad_rotation_id_blocks",
                  "time_based_ad_rotation_intervals",
                  "updated_time",
                  "use_new_app_click"]

        # List of all ad sets
        ad_sets = self.account.get_ad_sets(fields=fields)

        # Ad fields
        fields = ["id",
                  "account_id",
                  "ad_review_feedback",
                  "adlabels",
                  "adset",
                  "adset_id",
                  "bid_amount",
                  "bid_info",
                  "bid_type",
                  "campaign",
                  "campaign_id",
                  "configured_status",
                  "conversion_specs",
                  "created_time",
                  "creative",
                  "effective_status",
                  "issues_info",
                  "last_updated_by_app_id",
                  "name",
                  "recommendations",
                  "source_ad",
                  "status",
                  "tracking_specs",
                  "updated_time"]

        # List of all ads
        ads = self.account.get_ads(fields=fields)

        ad_tree = []
        for i in campaigns:
            ad_structure_dict = {"campaign": i.export_all_data(),
                                 "adset_list": []}

            a = 0
            for j in ad_sets:
                if j["campaign_id"] == i["id"]:
                    ad_structure_dict["adset_list"].append({"ad_set": j.export_all_data(),
                                                            "ad_list": []})

                    for k in ads:
                        if k["adset_id"] == j["id"]:
                            ad_structure_dict["adset_list"][a]["ad_list"].append({"ad": k.export_all_data()})

                    a += 1

            ad_tree.append(ad_structure_dict)

        return ad_tree

if __name__ == '__main__':
    app_id = <APP_ID>
    app_secret = <APP_SECRET>
    access_token = <ACCESS_TOKEN>
    ad_account_id = <AD_ACCOUNT_ID>

    NewAccount = LibFacebook(app_id, app_secret, access_token, ad_account_id)

    ad_tree = NewAccount.create_ad_tree()

    with open('ad_tree.json', 'w') as outfile:  
        json.dump(ad_tree, outfile, indent=4, sort_keys=True)

    print(ad_tree)
