from pysynthetic.synthesizers.regular.cgan.model import CGAN
from pysynthetic.synthesizers.regular.wgan.model import WGAN
from pysynthetic.synthesizers.regular.vanillagan.model import VanilllaGAN
from pysynthetic.synthesizers.regular.wgangp.model import WGAN_GP
from pysynthetic.synthesizers.regular.dragan.model import DRAGAN

__all__ = [
    "VanilllaGAN",
    "CGAN",
    "WGAN",
    "WGAN_GP",
    "DRAGAN"
]
