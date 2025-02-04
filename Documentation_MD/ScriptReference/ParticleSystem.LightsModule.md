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

# LightsModule

struct in UnityEngine

/

Implemented
in:[UnityEngine.ParticleSystemModule](UnityEngine.ParticleSystemModule.html)

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

[Switch to Manual](../Manual/class-ParticleSystem.html "Go to ParticleSystem
Component in the Manual")

### Description

Access the ParticleSystem Lights Module.

This module allows you to attach real-time Lights to a percentage of your
particles.  
  
The Lights Module is a simple and powerful module that allows particles to
cast light onto their environment easily. Lights can inherit properties from
the particles they are attached to, such as color and size. Point and Spot
Lights are supported, including shadow casting and Light cookies.

    
    
    using UnityEngine;
    using System.Collections;  
      
    [[RequireComponent](RequireComponent.html)(typeof([ParticleSystem](ParticleSystem.html)))]
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Light](Light.html) myLight;  
      
        void Start()
        {
            [ParticleSystem](ParticleSystem.html) ps = GetComponent<[ParticleSystem](ParticleSystem.html)>();
            var lights = ps.lights;
            lights.enabled = true;
            lights.ratio = 0.5f;
            lights.light = myLight;
        }
    }
    

### Properties

[alphaAffectsIntensity](ParticleSystem.LightsModule-
alphaAffectsIntensity.html)| Toggle whether the system multiplies the particle
alpha by the light intensity when it computes the final light intensity.  
---|---  
[enabled](ParticleSystem.LightsModule-enabled.html)| Specifies whether the
LightsModule is enabled or disabled.  
[intensity](ParticleSystem.LightsModule-intensity.html)| Define a curve to
apply custom intensity scaling to particle Lights.  
[intensityMultiplier](ParticleSystem.LightsModule-intensityMultiplier.html)|
Intensity multiplier.  
[light](ParticleSystem.LightsModule-light.html)| Select what Light Prefab you
want to base your particle lights on.  
[maxLights](ParticleSystem.LightsModule-maxLights.html)| Set a limit on how
many Lights this Module can create.  
[range](ParticleSystem.LightsModule-range.html)| Define a curve to apply
custom range scaling to particle Lights.  
[rangeMultiplier](ParticleSystem.LightsModule-rangeMultiplier.html)| Range
multiplier.  
[ratio](ParticleSystem.LightsModule-ratio.html)| Choose what proportion of
particles receive a dynamic light.  
[sizeAffectsRange](ParticleSystem.LightsModule-sizeAffectsRange.html)| Toggle
whether the system multiplies the particle size by the light range to
determine the final light range.  
[useParticleColor](ParticleSystem.LightsModule-useParticleColor.html)| Toggle
whether the particle lights multiply their color by the particle color.  
[useRandomDistribution](ParticleSystem.LightsModule-
useRandomDistribution.html)| Randomly assign Lights to new particles based on
ParticleSystem.LightsModule.ratio.  
  
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

