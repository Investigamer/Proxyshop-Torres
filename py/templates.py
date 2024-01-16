"""
* Torres Visuals Templates
"""
# Standard Library
from functools import cached_property
from typing import Optional, Callable

# Third Party
from photoshop.api._artlayer import ArtLayer
from photoshop.api._layerSet import LayerSet

# Local Imports
import src.helpers as psd
from src.enums.layers import LAYERS
from src.enums.mtg import pinlines_color_map
from src.frame_logic import contains_frame_colors
from src.templates import NormalTemplate, BorderlessMod, VectorTemplate, FullartMod
from src.utils.properties import auto_prop_cached

"""
* Normal Templates
"""


class TorresNinjaFullartTemplate (BorderlessMod, NormalTemplate):
    """Created by TorresVisuals."""
    template_suffix = 'Ninja'

    """
    * Bool Properties
    """

    @property
    def is_land(self) -> bool:
        return False

    """
    * Layer Properties
    """

    @property
    def twins_layer(self) -> Optional[ArtLayer]:
        return

    """
    * Methods
    """

    def enable_crown(self) -> None:
        """Simple one layer crown step."""
        self.crown_layer.visible = True


class TorresNeonTemplate (NormalTemplate):
    """Created by TorresVisuals."""
    template_suffix = 'Neon'

    """
    * Bool Properties
    """

    @property
    def is_land(self) -> bool:
        return False

    """
    * Layer Properties
    """

    @property
    def background_layer(self) -> Optional[ArtLayer]:
        return

    @property
    def twins_layer(self) -> Optional[ArtLayer]:
        return

    """
    METHODS
    """

    def enable_crown(self) -> None:
        """Simple one layer crown step."""
        self.crown_layer.visible = True


class TorresCrystalTemplate (BorderlessMod, NormalTemplate):
    """Created by TorresVisuals."""
    template_suffix = 'Crystal'

    """
    * Bool Properties
    """

    @property
    def is_land(self) -> bool:
        return False

    @property
    def is_legendary(self) -> bool:
        return False

    """
    * Layer Properties
    """

    @property
    def twins_layer(self) -> Optional[ArtLayer]:
        return

    """
    METHODS
    """

    def enable_frame_layers(self) -> None:
        super().enable_frame_layers()

        # Enable pinlines mask for PT
        if self.is_creature:
            psd.enable_mask(self.border_group)
            psd.enable_mask(self.pinlines_layer.parent)


class TorresBorderlessIkoriaTemplate (BorderlessMod, NormalTemplate):
    """Created by TorresVisuals."""
    template_suffix = 'Ikoria'

    """
    * Bool Properties
    """

    @property
    def is_land(self) -> bool:
        return False

    """
    * Layer Properties
    """

    @property
    def twins_layer(self) -> Optional[ArtLayer]:
        return

    """
    * Methods
    """

    def enable_frame_layers(self) -> None:
        super().enable_frame_layers()

        # Enable pinlines mask for PT
        if self.is_creature:
            psd.enable_mask(self.border_group)
            psd.enable_mask(self.pinlines_layer.parent)

    def enable_crown(self) -> None:
        """Simple one layer crown step."""
        self.crown_layer.visible = True


class TorresStainedGlassTemplate (NormalTemplate):
    """Created by TorresVisuals."""
    template_suffix = 'Stained Glass'

    """
    * Bool Properties
    """

    @property
    def is_land(self) -> bool:
        return False

    """
    * Layer Properties
    """

    @property
    def background_layer(self) -> Optional[ArtLayer]:
        return

    @property
    def twins_layer(self) -> Optional[ArtLayer]:
        return

    """
    * Methods
    """

    def enable_crown(self) -> None:
        """Simple one layer crown step."""
        self.crown_layer.visible = True


class TorresDragonTemplate (FullartMod, NormalTemplate):
    """Created by TorresVisuals."""
    template_suffix = 'Dragon'

    """
    * Bool Properties
    """

    @property
    def is_land(self) -> bool:
        return False

    """
    * Layer Properties
    """

    @property
    def twins_layer(self) -> Optional[ArtLayer]:
        return

    """
    * Methods
    """

    def enable_crown(self) -> None:
        """Simple one layer crown step."""
        self.crown_layer.visible = True


"""
* Basic Land Templates.
"""


class TorresSignatureBasicLandTemplate (VectorTemplate):
    """Created by TorresVisuals."""
    template_suffix = 'Signature'

    """
    * Mixin Methods
    """

    @auto_prop_cached
    def text_layer_methods(self) -> list[Callable]:
        """Only collector text layers."""
        return [self.collector_info, self.basic_text_layers]

    """
    * Frame Details
    """

    @cached_property
    def pinlines_colors(self) -> list[str]:
        """str: Only support W, U, B, R, G, dual colors, and 'Land' color."""
        if contains_frame_colors(self.pinlines):
            return list(self.pinlines)
        return [LAYERS.LAND]

    """
    * Layer Groups
    """

    @cached_property
    def pinlines_group(self) -> LayerSet:
        """LayerSet: Group containing pinline layers."""
        if self.is_snow:
            return psd.getLayerSet(LAYERS.SNOW)
        return psd.getLayerSet(LAYERS.PINLINES)

    """
    * Watermark and Expansion Symbols
    """

    def create_watermark(self) -> None:
        pass

    def create_basic_watermark(self) -> None:
        """Remove rules text step."""
        pass

    """
    * Text Layer Methods
    """

    def basic_text_layers(self) -> None:
        """Change some text layers to black color if card is non-colored 'Land' or 'Snow'."""
        if self.is_snow or not contains_frame_colors(self.pinlines):
            # FX and Color for name and typeline
            self.text_layer_name.textItem.color = self.RGB_BLACK
            self.text_layer_type.textItem.color = self.RGB_BLACK
            psd.disable_layer_fx(self.text_layer_name)
            psd.disable_layer_fx(self.text_layer_type)
        super().basic_text_layers()

    """
    * Frame Layer Methods
    """

    def enable_frame_layers(self) -> None:
        """Enable layers which make-up the frame of the card."""

        # PT Box
        if self.is_creature:
            self.pt_layer.visible = True

        # Pinlines
        self.generate_layer(
            group=self.pinlines_group,
            colors=self.pinlines_colors,
            masks=self.mask_layers)

        # Color Indicator -> Blended solid color layers
        if self.is_type_shifted:
            self.generate_layer(
                group=self.indicator_group,
                colors=self.indicator_colors,
                masks=self.indicator_masks)


class TorresJapaneseBasicLandTemplate (FullartMod, VectorTemplate):
    """Created by TorresVisuals."""
    template_suffix = 'Japanese'

    # Static Properties
    pinlines_color_map = {
        **pinlines_color_map,
        'W': [253, 245, 229],
        'U': [2, 107, 164],
        'B': [38, 42, 42],
        'R': [231, 76, 54],
        'G': [3, 112, 64]
    }

    """
    * Mixin Methods
    """

    @auto_prop_cached
    def text_layer_methods(self) -> list[Callable]:
        """Only collector text layers."""
        return [self.collector_info]

    """
    * Symbol Methods
    """

    def load_expansion_symbol(self) -> None:
        """Doesn't support Expansion Symbol."""
        return

    def create_watermark(self) -> None:
        """Build a watermark."""
        return

    def create_basic_watermark(self) -> None:
        """Builds a basic land watermark."""

        # Skip for 'Wastes'
        if self.pinlines == LAYERS.LAND:
            return

        # Enable the Japanese letter block
        group = psd.getLayerSet(LAYERS.SNOW if self.is_snow else 'Twins')
        psd.getLayer(self.pinlines, group).visible = True

    """
    * Frame Layer Methods
    """

    def enable_frame_layers(self) -> None:
        """Enable layers which make-up the frame of the card."""

        # Pinlines
        self.generate_layer(
            group=self.pinlines_group,
            colors=self.pinlines_colors,
            masks=self.mask_layers)
