[ ]()

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

LanguageEnglish

  * [English]()

  * C#

[ ](https://docs.unity3d.com)

## Scripting API

Version: Unity 6 Select a different version

LanguageEnglish

  * [English]()

#  [LightProbes](LightProbes.html).bakedProbes

Leave feedback

Suggest a change

## Success!

Thank you for helping us improve the quality of Unity Documentation. Although
we cannot accept all submissions, we do read each suggested change from our
users and will make updates where applicable.

Close

## Submission failed

For some reason your suggested change could not be submitted. Please <a>try
again</a> in a few minutes. And thank you for taking the time to help us
improve the quality of Unity Documentation.

Close

Your name Your email Suggestion* Submit suggestion

Cancel

[ ]()

public SphericalHarmonicsL2[] bakedProbes;

### Description

Coefficients of baked light probes.

Additional resources:
[SphericalHarmonicsL2](Rendering.SphericalHarmonicsL2.html).

    
    
    using UnityEngine;
    using UnityEngine.Rendering;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Color](Color.html) m_Ambient;
        public [Light](Light.html)[] m_Lights;  
      
        // This script adds the contribution of an ambient light and an array of lights to calculate new spherical harmonics
        // coefficients for all the baked light probes. You can use this for example in the [Editor](Editor.html) or at runtime to replace
        // the light probe coefficients that Unity bakes.
        void Start()
        {
            [SphericalHarmonicsL2](Rendering.SphericalHarmonicsL2.html)[] bakedProbes = LightmapSettings.lightProbes.bakedProbes;
            [Vector3](Vector3.html)[] probePositions = LightmapSettings.lightProbes.positions;
            int probeCount = LightmapSettings.lightProbes.count;
            for (int i = 0; i < probeCount; i++)
            {
                // Clear the probe and add ambient light
                bakedProbes[i].Clear();
                bakedProbes[i].AddAmbientLight(m_Ambient);
                
                // Add the contribution of directional and point lights
                foreach ([Light](Light.html) light in m_Lights)
                {
                    if (light.type == [LightType.Directional](LightType.Directional.html))
                    {
                        bakedProbes[i].AddDirectionalLight(-light.transform.forward, light.color, light.intensity);
                    }
                    else if (light.type == [LightType.Point](LightType.Point.html))
                    {
                        AddPointLight(probePositions[i], light, ref bakedProbes[i]);
                    }
                }
            }  
      
            LightmapSettings.lightProbes.bakedProbes = bakedProbes;
        }  
      
        void AddPointLight([Vector3](Vector3.html) probePosition, [Light](Light.html) light, ref [SphericalHarmonicsL2](Rendering.SphericalHarmonicsL2.html) sh)
        {
            // [Direction](UIElements.NavigationMoveEvent.Direction.html) from the light probe to the point light
            [Vector3](Vector3.html) probeToLight = light.transform.position - probePosition;
            
            // [Light](Light.html) attenuation between the point light and the light probe. This formula matches what Unity uses for
            // quadratic light attenuation.
            float attenuation = 1.0f / (1.0f + 25.0f * probeToLight.sqrMagnitude / (light.range * light.range));
            
            // With the normalized direction and the attenuation, the point light is equivalent to a directional
            // light in the context of a light probe.
            sh.AddDirectionalLight(probeToLight.normalized, light.color, light.intensity * attenuation);
        }
    }
    

Is something described here not working as you expect it to? It might be a
**Known Issue**. Please check with the Issue Tracker at
[issuetracker.unity3d.com](https://issuetracker.unity3d.com).

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from:
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://unity3d.com/learn) [Community
Answers](https://answers.unity3d.com) [Knowledge
Base](https://support.unity3d.com/hc/en-us)
[Forums](https://forum.unity3d.com) [Asset Store](https://unity3d.com/asset-
store) [Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)
[Legal](https://unity.com/legal) [Privacy
Policy](https://unity.com/legal/privacy-policy)
[Cookies](https://unity.com/legal/cookie-policy) [Do Not Sell or Share My
Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

