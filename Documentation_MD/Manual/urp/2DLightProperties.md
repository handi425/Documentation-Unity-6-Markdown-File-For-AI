[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/2DLightProperties.html)
  * [中文](/cn/current/Manual/urp/2DLightProperties.html)
  * [日本語](/ja/current/Manual/urp/2DLightProperties.html)
  * [한국어](/kr/current/Manual/urp/2DLightProperties.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/2DLightProperties.html)
  * [中文](/cn/current/Manual/urp/2DLightProperties.html)
  * [日本語](/ja/current/Manual/urp/2DLightProperties.html)
  * [한국어](/kr/current/Manual/urp/2DLightProperties.html)

  * [Working in Unity](../working-in-unity.html)
  * [2D in Unity](../Unity2D.html)
  * [2D game development in URP](../2d-urp-landing.html)
  * [2D lighting in URP](../urp/2d-index.html)
  * [Types of 2D lights](../urp/LightTypes.html)
  * Light 2D component reference for URP

[](../urp/create-light-2d.html)

Prepare your project for 2D lighting

[](../urp/2d-light-properties-explained.html)

Configure a 2D light

# Light 2D component reference for URP

Explore the properties and options to customize the appearance and behavior of
different Light 2D types. This page documents both the properties that are
common to all **Light 2D** types, and the different specific properties and
options available for each **Light 2D** type.

![](../../uploads/urp/2D/2DLightBasics.png) Property | Function  
---|---  
**Light Type** | Select the type of Light you want the selected Light to be. The available types are **Freeform** , **Sprite** , **Spot** , and **Global**.  
**Color** | Use the color picker to set the color of the emitted light.  
**[Intensity](2d-light-properties-explained.html#intensity)** | Enter the desired brightness value of the Light. The default value is 1.  
**Target Sorting Layers** | Select the sorting layers that this Light targets and affects.  
**[Blend Style](LightBlendStyles.html)** | Select the blend style used by this Light. You can customize different blend styles in the [2D Renderer Asset](2DRendererData-overview.html).  
**[Light Order](2d-light-properties-explained.html#light-order)** (unavailable for **Global Lights**) | Enter a value here to specify the rendering order of this Light relative to other Lights on the same sorting layer(s). Lights with lower values are rendered first, and negative values are valid.  
**[Overlap Operation](2d-light-properties-explained.html#overlap-operation)** | Select the overlap operation used by this light The operations available are **Additive** , and **Alpha Blend**.  
**Shadow Strength** | Use the slider to control the amount of light that **Shadow Caster 2Ds** block when they obscure this Light. The value scales from 0 (no light is blocked) to 1 (all light is blocked).  
**Volumtric Intensity** | Use the slider to select the opacity of the volumetric lighting. The value scales from 0 (transparent) to 1 (opaque).  
**Volumetric Shadow Strength** | Use the slider to control the amount of volumetric light that **Shadow Caster 2Ds** block when they obscure this Light. The value scales from 0 (no light is blocked) to 1 (all light is blocked).  
**[Normal Map Quality](2d-light-properties-explained.html#quality)** | Select either **Disabled** (default), **Accurate** or **Fast** to adjust the accuracy of the lighting calculations used.  
**[Normal Map Distance](2d-light-properties-explained.html#distance)** (available when **Use Normal Map** quality is enabled) | Enter the desired distance (in Unity units) between the Light and the lit Sprite. This does not Transform the position of the Light in the **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](../CreatingScenes.html)  
See in [Glossary](../Glossary.html#Scene).  
  
## Specific properties of each type of Light 2D

Learn which type of light is the best fit for your project by comparing the
different options of the different **Light 2D** types:

  * Freeform
  * SpriteA 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](../sprite/sprite-landing.html)  
See in [Glossary](../Glossary.html#Sprite)

  * Spot
  * Global

**Important:** The Parametric Light Type is deprecated from URP 11 onwards. To
convert existing Parametric lights to Freeform lights, go to **Window** >
**Rendering** > **Render Pipeline Converter** , change tab to **Upgrade 2D
(URP) Assets** and enable the converter **Parametric To Freeform Light
Upgrade**.

## Freeform

![Freeform Properties](../../uploads/urp/2D/LightType_Freeform.png) Freeform
Properties

Select the **Freeform** Light type to create a Light from an editable polygon
with a spline editor. To begin editing your shape, select the Light and find
the ![](../../uploads/urp/2D/image_20.png)button in its **Inspector** A Unity
window that displays information about the currently selected GameObject,
asset or project settings, allowing you to inspect and edit the values. [More
info](../UsingTheInspector.html)  
See in [Glossary](../Glossary.html#Inspector) window. Select it to enable the
shape editing mode.

Add new control points by clicking the mouse along the inner polygon’s
outline. Remove control points selecting the point and pressing the Delete
key.

The following additional properties are available to the **Freeform** Light
type.

Property | Function  
---|---  
**Falloff** | Adjusts the falloff area of this light. The higher the falloff value, the larger area the falloff spans.  
**Falloff Strength** | Adjusts the falloff curve to control the softness of this light’s edges. The higher the falloff strength, the softer the edges of this light.  
![Light Editing Mode](../../uploads/urp/2D/image_21.png) | ![Light Effect](../../uploads/urp/2D/image_22.png)  
---|---  
Freeform Light in edit mode | Resulting Light Effect  
  
When creating a **Freeform** Light, take care to avoid self-intersection as
this may cause unintended lighting results. Self-intersection may occur by
creating outlines where edges cross one another, or by enlarging falloff until
it overlaps itself. To prevent such issues, it is recommended to edit the
shape of the Light until the conditions creating the self-intersection no
longer occur.

![Freeform Self Intersection](../../uploads/urp/2D/2D_FreeformOutlineIntersection0.png) | ![Freeform Self Intersection](../../uploads/urp/2D/2D_FreeformOutlineIntersection1.png)  
---|---  
Outline self-intersection in Edit mode. | Light effect with a black triangular artifact  
![Freeform Self Intersection](../../uploads/urp/2D/2D_FreeformFalloffIntersection0.png) | ![Freeform Self Intersection](../../uploads/urp/2D/2D_FreeformFalloffIntersection1.png)  
---|---  
Falloff overlap in Edit mode | Light effect with double lighted areas with overlapping falloff  
  
## Sprite

Select the **Sprite** Light type to create a Light based on a selected Sprite
by assigning the selected Sprite to the additional Sprite property.

![The Sprite property](../../uploads/urp/2D/LightType_Sprite.png) The Sprite property Property | Function  
---|---  
**Sprite** | Select a Sprite as the Light source.  
![Selected Sprite](../../uploads/urp/2D/image_24.png) | ![Resulting Light effect](../../uploads/urp/2D/image_25.png)  
---|---  
Selected Sprite | Resulting Light effect  
  
## Spot

Select the **Spot** Light type for great control over the angle and direction
of the selected Light with the following additional properties.

![Point Light properties](../../uploads/urp/2D/LightType_Point.png) Point Light properties Property | Function  
---|---  
**Radius Inner** | Set the inner radius here or with the **gizmo** A graphic overlay associated with a GameObject in a Scene, and displayed in the Scene View. Built-in scene tools such as the move tool are Gizmos, and you can create custom Gizmos using textures or scripting. Some Gizmos are only drawn when the GameObject is selected, while other Gizmos are drawn by the Editor regardless of which GameObjects are selected. [More info](../GizmosMenu.html#GizmosIcons)  
See in [Glossary](../Glossary.html#Gizmo). Light within the inner radius will
be at maximum [intensity](2d-light-properties-explained.html#intensity).  
**Radius Outer** | Set the outer radius here or with the gizmo. Light intensity decreases to zero as it approaches the outer radius.  
**Inner / Outer Spot Angle** | Set the angles with this slider or with the gizmo. Light within the inner and outer angles will be at the intensity specified by inner and outer radius.  
![Point Light editing Mode](../../uploads/urp/2D/image_27.png) | ![Resulting light effect](../../uploads/urp/2D/image_28.png)  
---|---  
Point Light in Edit mode | Resulting Light effect  
  
## Global

Global Lights light all objects on the [targeted sorting layers](2d-light-
properties-explained.html#target-sorting-layers). Only one global Light can be
used per [Blend Style](LightBlendStyles.html), and per sorting layer.

## Additional resources

  * [Configure a 2D light](2d-light-properties-explained.html)
  * [Light Blend Styles component reference](LightBlendStyles.html)

[](../urp/create-light-2d.html)

Prepare your project for 2D lighting

[](../urp/2d-light-properties-explained.html)

Configure a 2D light

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

