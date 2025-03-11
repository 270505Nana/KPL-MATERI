from enum import enum

class StudentStatusState(Enum):
    TERDAFTAR = "terdaftar"
    CUTI = "Cuti"
    AKTIF = "Aktif"
    LULUS = "Lulus"

# Trigger input
class TriggerInputState(Enum):
    CETAK_KSM = "Cetak ksm"
    MENYELESAIKAN_CUTI = "Menyelesaikan cuti"
    LULUS = "lulus"
    MENGAJUKAN_CUTI = "mengajukan cuti"

# transition
state_transitions = {
    StudentStatusState.TERDAFTAR:{
        TriggerInputState.CETAK_KSM: StudentStatusState.AKTIF,
        TriggerInputState.MENGAJUKAN_CUTI: StudentStatusState.CUTI
    },
    StudentStatusState.CUTI:{
        TriggerInputState.MENYELESAIKAN_CUTI: StudentStatusState.TERDAFTAR
    },
    StudentStatusState.AKTIF:{
        TriggerInputState.LULUS: StudentStatusState.LULUS,
        TriggerInputState.MENGAJUKAN_CUTI: StudentStatusState.CUTI
    },
}

def change_state(current_state, trigger_input):
    cond_1 = current_state in state_transitions 
    cond_2 = trigger_input in state_transitions[current_state]
    if cond_1 and cond_2:
        # terdaftar, aktif, lulu, cuti
        return state_transitions[current_state][trigger_input]
    return "Transisi tidak valid"

# belum selese tapi