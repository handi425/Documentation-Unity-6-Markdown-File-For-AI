[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/shared/lens-flare/lens-flare-srp-reference.html)
  * [中文](/cn/current/Manual/urp/shared/lens-flare/lens-flare-srp-reference.html)
  * [日本語](/ja/current/Manual/urp/shared/lens-flare/lens-flare-srp-reference.html)
  * [한국어](/kr/current/Manual/urp/shared/lens-flare/lens-flare-srp-reference.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/shared/lens-flare/lens-flare-srp-reference.html)
  * [中文](/cn/current/Manual/urp/shared/lens-flare/lens-flare-srp-reference.html)
  * [日本語](/ja/current/Manual/urp/shared/lens-flare/lens-flare-srp-reference.html)
  * [한국어](/kr/current/Manual/urp/shared/lens-flare/lens-flare-srp-reference.html)

  * [Visual effects](../../../visual-effects.html)
  * [Lens flares](../../../visual-effects-lens-flares.html)
  * [Lens flares in URP](../../../urp/shared/lens-flare/lens-flare.html)
  * Lens Flare (SRP) component reference for URP

[](../../../urp/shared/lens-flare/post-processing-screen-space-lens-
flare.html)

Add screen space lens flares in URP

[](../../../urp/shared/lens-flare/lens-flare-asset.html)

Lens Flare (SRP) Data Asset in URP

# Lens Flare (SRP) component reference for URP

Refer to [Add lens flares](lens-flare-component.html) for information on how
to use the **Lens Flare** A component that simulates the effect of lights
refracting inside a camera lens. Use a Lens Flare to represent very bright
lights or add atmosphere to your scene. [More info](../../../class-
LensFlare.html)  
See in [Glossary](../../../Glossary.html#LensFlare) (SRP) component.

## General

**Property** | **Description**  
---|---  
**Lens Flare Data** | Select the [Lens Flare (SRP) Data](lens-flare-asset.html) asset this component controls.  
**Intensity** | Multiplies the intensity of the lens flare.  
**Scale** | Multiplies the scale of the lens flare.  
**Light Override** | Specifies the light component Unity gets the color and shape values from, if you enable **Modulate By Light Color** or **Attenuation By Light Shape**. If you don’t specify a light component, Unity uses the Light component from this **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](../../../class-GameObject.html)  
See in [Glossary](../../../Glossary.html#GameObject).  
**Attenuation by Light Shape** | Enable this property to automatically change the appearance of the lens flare based on the type of light you attached this component to.  
For example, if this component is attached to a spot light and the camera is
looking at this light from behind, the lens flare is not visible.  
This property is only available when this component is attached to a light.  
**Attenuation Distance** | The distance between the start and the end of the Attenuation Distance Curve.  
This value operates between 0 and 1 in world space.  
**Attenuation Distance Curve** | Fades out the appearance of the lens flare over the distance between the GameObject this asset is attached to, and the **Camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](../../../CamerasOverview.html)  
See in [Glossary](../../../Glossary.html#Camera).  
**Scale Distance** | The distance between the start and the end of the **Scale Distance Curve**.  
This value operates between 0 and 1 in world space.  
**Scale Distance Curve** | Changes the size of the lens flare over the distance between the GameObject this asset is attached to, and the Camera.  
**Screen Attenuation Curve** | Reduces the effect of the lens flare based on its distance from the edge of the screen. You can use this to display a lens flare at the edge of your screen  
  
## Occlusion

**Property** | **Description**  
---|---  
**Enable** | Enable this property to partially obscure the lens flare based on the **depth buffer** A memory store that holds the z-value depth of each pixel in an image, where the z-value is the depth for each rendered pixel from the projection plane. [More info](../../../class-RenderTexture.html)  
See in [Glossary](../../../Glossary.html#depthbuffer)  
**Occlusion Radius** | Defines how far from the light source Unity occludes the lens flare. This value is in world space.  
**Sample Count** | The number of random samples the CPU uses to generate the **Occlusion Radius.**  
**Occlusion Offset** | Offsets the plane that the occlusion operates on. A higher value moves this plane closer to Camera. This value is in world space.   
For example, if a lens flare is inside the light bulb, you can use this to
sample occlusion outside the light bulb.  
**Occlusion Remap Curve** | Allow the occlusion [from 0 to 1] to be remap with any desired shape.  
**Allow Off Screen** | Enable this property to allow lens flares outside the Camera’s view to affect the current field of view.  
  
[](../../../urp/shared/lens-flare/post-processing-screen-space-lens-
flare.html)

Add screen space lens flares in URP

[](../../../urp/shared/lens-flare/lens-flare-asset.html)

Lens Flare (SRP) Data Asset in URP

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

