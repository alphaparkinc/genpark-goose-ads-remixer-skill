class GooseAdsRemixerClient:
    def remix_ad(self, winning_copy_sample: str, target_channel: str) -> dict:
        return {"remixed_copy": f"[{target_channel.upper()} REMIX]: {winning_copy_sample} -- Check out today!"}