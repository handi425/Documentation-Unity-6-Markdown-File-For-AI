[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/ProgressiveLightmapper-CustomFallOff.html)
  * [中文](/cn/current/Manual/ProgressiveLightmapper-CustomFallOff.html)
  * [日本語](/ja/current/Manual/ProgressiveLightmapper-CustomFallOff.html)
  * [한국어](/kr/current/Manual/ProgressiveLightmapper-CustomFallOff.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/ProgressiveLightmapper-CustomFallOff.html)
  * [中文](/cn/current/Manual/ProgressiveLightmapper-CustomFallOff.html)
  * [日本語](/ja/current/Manual/ProgressiveLightmapper-CustomFallOff.html)
  * [한국어](/kr/current/Manual/ProgressiveLightmapper-CustomFallOff.html)

  * [Lighting](LightingOverview.html)
  * [Direct and indirect lighting](direct-and-indirect-lighting.html)
  * [Precalculating surface lighting with lightmaps](Lightmapping-landing.html)
  * [Configuring lightmapping](configure-lightmapping-settings.html)
  * Change the fade distance of lights with fall-off

[](global-illumination-configure.html)

Configure lightmapping with a Lighting Settings Asset

[](LightmappingDirectional.html)

Store light direction with Directional Mode

# Change the fade distance of lights with fall-off

In the real world, light fades over distance, and dim lights have a lower
range than bright lights. The term “fall-off” refers to the rate at which
light fades. Alongside Unity’s default fall-off lighting behaviour, you can
also use custom fall-off settings.

Progressive **Lightmapper** A tool in Unity that bakes lightmaps according to
the arrangement of lights and geometry in your scene. [More
info](Lightmapping.html)  
See in [Glossary](Glossary.html#Lightmapper) provides custom fall-off presets,
which you can implement via script. See the image below the table for a visual
representation of how these work, and the code sample below the image for an
example of how to use this functionality.

Refer to
[`FalloffType`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GlobalIllumination.FalloffType.html)
for more information.

![An example of the visual effect of each custom fall-off
preset](../uploads/Main/ProgressiveLightmapper-CustomFallOff.jpg) An example
of the visual effect of each custom fall-off preset

## Example

**Note** : The code example below only works with the Progressive Lightmapper
when you use Baked or Mixed lights. To use the code example with **realtime
lights** Light components whose Mode property is set to Realtime. Unity
calculates and updates the lighting of Realtime Lights every frame at runtime.
No Realtime Lights are precomputed. [More info](LightModes-
introduction.html#realtime)  
See in [Glossary](Glossary.html#RealtimeLights), use [Enlighten Realtime
Global Illumination](realtime-gi-using-enlighten.html).

    
    
    using System.Collections;
    using System.Collections.Generic;
    using UnityEngine;
    using UnityEngine.Experimental.GlobalIllumination;
    using UnityEngine.SceneManagement;
    [ExecuteInEditMode]
    public class ExtractFalloff : MonoBehaviour
    {
        public void OnEnable()
        {
            Lightmapping.RequestLightsDelegate testDel = (Light[] requests, Unity.Collections.NativeArray<LightDataGI> lightsOutput) =>
            {
                DirectionalLight dLight = new DirectionalLight();
                PointLight point = new PointLight();
                SpotLight spot = new SpotLight();
                RectangleLight rect = new RectangleLight();
                DiscLight disc = new DiscLight();
                Cookie cookie = new Cookie();
                LightDataGI ld = new LightDataGI();
                
                for (int i = 0; i < requests.Length; i++)
                {
                    Light l = requests[i];
                    switch (l.type)
                    {
                        case UnityEngine.LightType.Directional: LightmapperUtils.Extract(l, ref dLight); LightmapperUtils.Extract(l, out cookie); ld.Init(ref dLight, ref cookie); break;
                        case UnityEngine.LightType.Point: LightmapperUtils.Extract(l, ref point); LightmapperUtils.Extract(l, out cookie); ld.Init(ref point, ref cookie); break;
                        case UnityEngine.LightType.Spot: LightmapperUtils.Extract(l, ref spot); LightmapperUtils.Extract(l, out cookie); ld.Init(ref spot, ref cookie); break;
                        case UnityEngine.LightType.Rectangle: LightmapperUtils.Extract(l, ref rect); LightmapperUtils.Extract(l, out cookie); ld.Init(ref rect, ref cookie); break;
                        case UnityEngine.LightType.Disc: LightmapperUtils.Extract(l, ref disc); LightmapperUtils.Extract(l, out cookie); ld.Init(ref disc, ref cookie); break;
                        default: ld.InitNoBake(l.GetInstanceID()); break;
                    }
    
                    if (l.cookie != null)
                    {
                        ld.cookieID = l.cookie.GetInstanceID();
                    }
                    else
                    {
                        ld.cookieID = 0;
                    }
                    
                    ld.falloff = FalloffType.InverseSquared;
                    lightsOutput[i] = ld;
                }
            };
            Lightmapping.SetDelegate(testDel);
        }
        void OnDisable()
        {
            Lightmapping.ResetDelegate();
        }
    }
    

**Note** : All code in the example above is necessary for the custom falloff
to work; however, you can change `InverseSquared` in the line `ld.falloff =
FalloffType.InverseSquared;` to use any of [the
presets](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GlobalIllumination.FalloffType.html).

* * *

Progressive Lightmapper added in
[2018.1](https://docs.unity3d.com/2018.1/Documentation/Manual/30_search.html?q=newin20181)
NewIn20181

2018–03–28 Page published

[](global-illumination-configure.html)

Configure lightmapping with a Lighting Settings Asset

[](LightmappingDirectional.html)

Store light direction with Directional Mode

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

