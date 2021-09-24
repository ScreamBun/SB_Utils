"""
OSQuery kva_speculative_info ORM
"""
from osquery_orm.orm import BaseModel
from peewee import IntegerField


class KvaSpeculativeInfo(BaseModel):
    """
    Display kernel virtual address and speculative execution information for the system.
    Examples:
        select * from kva_speculative_info
    """
    # Kernel Virtual Address shadowing is enabled.
    kva_shadow_enabled = IntegerField()
    # User pages are marked as global.
    kva_shadow_user_global = IntegerField()
    # Kernel VA PCID flushing optimization is enabled.
    kva_shadow_pcid = IntegerField()
    # Kernel VA INVPCID is enabled.
    kva_shadow_inv_pcid = IntegerField()
    # Branch Prediction mitigations are enabled.
    bp_mitigations = IntegerField()
    # Branch Predictions are disabled via system policy.
    bp_system_pol_disabled = IntegerField()
    # Branch Predictions are disabled due to lack of microcode update.
    bp_microcode_disabled = IntegerField()
    # SPEC_CTRL MSR supported by CPU Microcode.
    cpu_spec_ctrl_supported = IntegerField()
    # Windows uses IBRS.
    ibrs_support_enabled = IntegerField()
    # Windows uses STIBP.
    stibp_support_enabled = IntegerField()
    # PRED_CMD MSR supported by CPU Microcode.
    cpu_pred_cmd_supported = IntegerField()

    class Meta:
        table_name = "kva_speculative_info"
