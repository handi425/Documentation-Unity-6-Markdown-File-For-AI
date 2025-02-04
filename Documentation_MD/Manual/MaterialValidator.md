[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/MaterialValidator.html)
  * [中文](/cn/current/Manual/MaterialValidator.html)
  * [日本語](/ja/current/Manual/MaterialValidator.html)
  * [한국어](/kr/current/Manual/MaterialValidator.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/MaterialValidator.html)
  * [中文](/cn/current/Manual/MaterialValidator.html)
  * [日本語](/ja/current/Manual/MaterialValidator.html)
  * [한국어](/kr/current/Manual/MaterialValidator.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Materials](Materials.html)
  * [Material Validator in the Built-In Render Pipeline](materials-troubleshooting.html)
  * Material Validator window reference for the Built-In Render Pipeline

[](material-validator-make-shader-compatible.html)

Make a shader compatible with the Material Validator in the Built-In Render
Pipeline

[](class-Material.html)

Material Inspector window reference

# Material Validator window reference for the Built-In Render Pipeline

## Validate Albedo mode

![The PBR Validation Settings when in Validate Albedo mode, which appear in
the scene view](../uploads/Main/materialValidator3.png) The PBR Validation
Settings when in Validate Albedo mode, which appear in the scene view

The PBR Validation Settings that appear in the **Scene** A Scene contains the
environments and menus of your game. Think of each unique Scene file as a
unique level. In each Scene, you place your environments, obstacles, and
decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) view when you set Material Validation
to Validate Albedo.

**Property:** | **Function:**  
---|---  
**Check Pure Metals** | Enable this checkbox if you want the Material Validator to highlight in yellow any **pixels** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](ShadowPerformance.html)  
See in [Glossary](Glossary.html#pixel) it finds which Unity defines as
metallic, but which have a non-zero albedo value. See [Pure Metals](material-
validator-validate.html#pureMetals) for more details. By default, this is not
enabled.  
**Luminance Validation** | Use the drop-down to select a preset configuration for the Material Validator. If you select any option other than **Default Luminance** , you can also adjust the Hue Tolerance and Saturation Tolerance. The color bar underneath the name of the property indicates the albedo color of the configuration. The Luminance value underneath the drop-down indicates the minimum and maximum luminance value. The Material Validator highlights any pixels with a luminance value outside of these values. This is set to **Default Luminance** by default.  
**Hue Tolerance** | When checking the albedo color values of your material, this slider allows you to control the amount of error allowed between the hue of your material, and the hue in the validation configuration.  
Saturation Tolerance | When checking the albedo color values of your material, this slider allows you to control the amount of error allowed between the saturation of your material, and the saturation in the validation configuration.  
**Color Legend** | These colors correspond to the colours that the Material Validator displays in the **Scene view** An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object. [More info](UsingTheSceneView.html)  
See in [Glossary](Glossary.html#SceneView) when the pixels for that Material
are outside the defined values.  
|  **Red** Below Minimum Luminance Value | The Material Validator highlights in red any pixels which are below the minimum luminance value defined in **Luminance Validation** (meaning that they are too dark).  
|  **Blue** Above Maximum Luminance Value | The Material Validator highlights in blue any pixels which are above the maximum luminance value defined in **Luminance Validation** (meaning that they are too bright).  
|  **Yellow** Not A Pure Metal | If you have Check Pure Metals enabled, the Material Validator highlights in yellow any pixels which Unity defines as metallic, but which have a non-zero albedo value. See Pure Metals, below, for more details.  
  
## Validate Metal Specular mode

![The PBR validations settings, when in Validate Metal Specular
mode](../uploads/Main/materialValidator6.png) The PBR validations settings,
when in Validate Metal Specular mode

The PBR Validation Settings that appear in the Scene view when you set
**Material Validation** to **Validate Metal Specular**.

**_Property:_** | **_Function:_**  
---|---  
**Check Pure Metals** | Enable this checkbox if you want the Material Validator to highlight in yellow any pixels it finds which Unity defines as metallic, but which have a non-zero albedo value. See Pure Metals, below, for more details. By default, this is not enabled.  
**Color Legend** | These colors correspond to the colours that the Material Validator displays in the Scene view when the pixels for that Material are invalide - meaning their specular value falls outside the valid range for that type of material (metallic or non-metallic). See below this table for the valid ranges.  
|  **Blue** Below Minimum Specular Value | The Material Validator highlights in red any pixels which are below the minimum specular value. (40 for non-metallic, or 155 for metallic).  
|  **Red** Above Maximum Specular Value | The Material Validator highlights in blue any pixels which are above the maximum specular value. (75 for non-metallic, or 255 for metallic).  
|  **Yellow** Not A Pure Metal | If you have **Check Pure Metals** enabled, the Material Validator highlights in yellow any pixels which Unity defines as metallic, but which have a non-zero albedo value. See Pure Metals, below, for more details.  
  
## Additional resources

  * [Material Validator](material-validator-introduction.html)

[](material-validator-make-shader-compatible.html)

Make a shader compatible with the Material Validator in the Built-In Render
Pipeline

[](class-Material.html)

Material Inspector window reference

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

