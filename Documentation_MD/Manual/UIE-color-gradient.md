[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-color-gradient.html)
  * [中文](/cn/current/Manual/UIE-color-gradient.html)
  * [日本語](/ja/current/Manual/UIE-color-gradient.html)
  * [한국어](/kr/current/Manual/UIE-color-gradient.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-color-gradient.html)
  * [中文](/cn/current/Manual/UIE-color-gradient.html)
  * [日本語](/ja/current/Manual/UIE-color-gradient.html)
  * [한국어](/kr/current/Manual/UIE-color-gradient.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Work with text](UIE-work-with-text.html)
  * Color gradients

[](UIE-sprite-asset-properties.html)

Sprite Asset properties reference

[](UIE-color-emojis.html)

Color emojis

# Color gradients

You can apply gradients of up to four colors to text. When you add a color
gradient, TextCore applies gradient colors to each character in a text string.

Use the [`<gradient>` rich text tags](UIE-supported-tags.html#gradient) to
apply color gradient presets to text objects. A gradient preset overrides the
text’s local gradient type and colors.

## Create a color gradient preset

To create a color gradient with one or more colors, and place it in a specific
folder, follow these steps:

  1. From the menu, select **Assets** > **create** > **Text Core** > **Color Gradient** to add a new color gradient preset.

  2. In the Color Gradient’s **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) window, select a color mode from
the dropdown menu:

     * **Single** : Applies a single color.
     * **Horizontal Gradient** : Applies two colors and produces a side-to-side transition between them on each character.
     * **Vertical Gradient** : Applies two colors and produces an up-and-down transition between the two on each character.
     * **Four Corners Gradient:** Applies four colors. Each color radiates from its assigned corner of each character.
  3. Set the gradient colors. The number of colors available in the **Colors** field depends on the gradient mode you choose. Each swatch corresponds to the color’s origin on a character **sprite** A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](sprite/sprite-landing.html)  
See in [Glossary](Glossary.html#Sprite).

  4. Place the color gradient asset into the path set for the **Color Gradient Presets** in the [Panel Text Setting asset](UIE-text-setting-asset.html#color-gradients-presets).

## Apply color gradient presets

To apply a color gradient preset to text, reference the color gradient by name
as `<gradient="name-of-the-color-gradient">Your text</gradient>`. If you apply
the color gradient like this, the color of the text is multiplied by the
object’s current vertex colors.

To apply the pure gradient to a selection of text, use a `<color>` tag to
reset the color to white. For example:

    
    
    <color=white><gradient="Light to Dark Green - Vertical">Light to Dark Green gradient</gradient></color>
    

## Color gradient mode examples

The following shows color gradient examples for each mode.

### Single color

A single-color gradient.

![Text with each character in
yellow.](../uploads/Main/font/ColorGradient_Single-Y_half.png) Text with each
character in yellow.

### Horizontal gradients

A side-to-side gradient with two colors.

![Text with color transition from yellow to black side-to-side for each
character.](../uploads/Main/font/ColorGradient_Horiz-YB_half.png) Text with
color transition from yellow to black side-to-side for each character. ![Text
with color transition from black to yellow side-to-side for each
character.](../uploads/Main/font/ColorGradient_Horiz-BY_half.png) Text with
color transition from black to yellow side-to-side for each character.

### Vertical gradients

An up-and-down gradient with two colors.

![Text with color transition from black to yellow up-and-down for each
character.](../uploads/Main/font/ColorGradient_Vert-BY_half.png) Text with
color transition from black to yellow up-and-down for each character. ![Text
with color transition from yellow to black up-and-down for each
character.](../uploads/Main/font/ColorGradient_Vert-YB_half.png) Text with
color transition from yellow to black up-and-down for each character.

### Four corner gradients

A gradient with four colors. Each color radiates from one corner. This is the
most versatile gradient type. You can vary some colors and keep others
identical to create different kinds of gradients.

![Text with four-color gradient for each character with yellow on the up-left,
black on the up-right, red on the down-left, and green on the down-right.
](../uploads/Main/font/ColorGradient_4-Corner-YBRG_half.png) Text with four-
color gradient for each character with yellow on the up-left, black on the up-
right, red on the down-left, and green on the down-right.

This example shows three corners with one color and the fourth with a
different color.

![Text with four-color gradient for each character with black on the up-left
and yellow for the other
corners.](../uploads/Main/font/ColorGradient_1-Corner-BYYY_half.png) Text with
four-color gradient for each character with black on the up-left and yellow
for the other corners.

This example shows pairs of adjacent corners with the same color to create
horizontal or vertical gradients.

![Text with four-color gradient for each character with black on the left up
and down, and yellow on the right up and
down.](../uploads/Main/font/ColorGradient_2-Corner-BYBY_half.png) Text with
four-color gradient for each character with black on the left up and down, and
yellow on the right up and down. ![Text with four-color gradient for each
character with black on the up left and right, and yellow on the down left and
right.](../uploads/Main/font/ColorGradient_2-Corner-BBYY_half.png) Text with
four-color gradient for each character with black on the up left and right,
and yellow on the down left and right.

This example shows pairs of diagonally opposite corners the same color to
create diagonal gradients.

![Text with four-color gradient for each character with black on the up-left
and down-right, and yellow on the up-right and down-
left.](../uploads/Main/font/ColorGradient_2-Corner-BYYB_half.png) Text with
four-color gradient for each character with black on the up-left and down-
right, and yellow on the up-right and down-left. ![Text with four-color
gradient for each character with yellow on the up-left and down-right, and
black on the up-right and down-
left.](../uploads/Main/font/ColorGradient_2-Corner-YBBY_half.png) Text with
four-color gradient for each character with yellow on the up-left and down-
right, and black on the up-right and down-left.

This example creates horizontal and vertical three-color gradients with a
dominant color at one end and a transition between two colors at the other.

![Text with four-color gradient for each character with yellow on the left up
and down, red on the up-right, and black on the down-
right.](../uploads/Main/font/ColorGradient_3-Corner-YRYB_half.png) Text with
four-color gradient for each character with yellow on the left up and down,
red on the up-right, and black on the down-right. ![Text with four-color
gradient for each character with yellow on the up left and right, red on the
down-left, and black on the down-
right.](../uploads/Main/font/ColorGradient_3-Corner-YYRB_half.png) Text with
four-color gradient for each character with yellow on the up left and right,
red on the down-left, and black on the down-right.

This example gives two diagonally opposite corners the same color and the
other two corners different colors to create a diagonal stripe three-color
gradient.

![Text with four-color gradient for each character with red on the up-left,
yellow on the up-right and down-left, and black on the down-
right.](../uploads/Main/font/ColorGradient_3-Corner-RYYB_half.png) Text with
four-color gradient for each character with red on the up-left, yellow on the
up-right and down-left, and black on the down-right. ![Text with four-color
gradient for each character with yellow on the up-left and down-right, black
on the up-right, and red on the down-
left.](../uploads/Main/font/ColorGradient_3-Corner-YBRY_half.png) Text with
four-color gradient for each character with yellow on the up-left and down-
right, black on the up-right, and red on the down-left.

## Additional resources

  * [Rich text tags](UIE-rich-text-tags.html)
  * [Supported rich text tags](UIE-supported-tags.html)
  * [Style sheets assets](UIE-style-sheet.html)
  * [Sprites assets](UIE-sprite.html)

[](UIE-sprite-asset-properties.html)

Sprite Asset properties reference

[](UIE-color-emojis.html)

Color emojis

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://learn.unity.com/)[Community
Answers](https://answers.unity3d.com)[Knowledge
Base](https://support.unity3d.com/hc/en-
us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-
store)[Terms of
use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy
Policy](https://unity.com/legal/privacy-
policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share
My Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

