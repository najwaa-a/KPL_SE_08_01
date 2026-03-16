from enum import Enum

class VendingMachineState(Enum):
    IDLE = "Idle"
    MENUNGGU_PRODUK = "Menunggu Produk"
    MENGELUARKAN_PRODUK = "Mengeluarkan Produk"
    SELESAI = "Selesai"

class Trigger(Enum):
    MASUKKAN_UANG = "Masukkan Uang"
    PILIH_PRODUK = "Pilih Produk"
    KELUARKAN_PRODUK = "Keluarkan Produk"
    RESET = "Reset"

transitions = {
    VendingMachineState.IDLE: {
        Trigger.MASUKKAN_UANG: VendingMachineState.MENUNGGU_PRODUK
    },
    VendingMachineState.MENUNGGU_PRODUK: {
        Trigger.PILIH_PRODUK: VendingMachineState.MENGELUARKAN_PRODUK
    },
    VendingMachineState.MENGELUARKAN_PRODUK: {
        Trigger.KELUARKAN_PRODUK: VendingMachineState.SELESAI
    },
    VendingMachineState.SELESAI: {
        Trigger.RESET: VendingMachineState.IDLE
    }
}

def change_state(current_state, trigger):
    if current_state in transitions and trigger in transitions[current_state]:
        return transitions[current_state][trigger]
    return "Transisi tidak valid"


current_state = VendingMachineState.IDLE
print(f"State awal: {current_state.value}")

current_state = change_state(current_state, Trigger.MASUKKAN_UANG)
print(f"Setelah Masukkan Uang: {current_state.value}")

current_state = change_state(current_state, Trigger.PILIH_PRODUK)
print(f"Setelah Pilih Produk: {current_state.value}")

current_state = change_state(current_state, Trigger.KELUARKAN_PRODUK)
print(f"Setelah Keluarkan Produk: {current_state.value}")

current_state = change_state(current_state, Trigger.RESET)
print(f"Setelah Reset: {current_state.value}")