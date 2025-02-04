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

#
[ParticleSystem.TrailModule](ParticleSystem.TrailModule.html).colorOverTrail

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

public [ParticleSystem.MinMaxGradient](ParticleSystem.MinMaxGradient.html)
colorOverTrail;

### Description

The gradient that controls the trail colors over the length of the trail.

Additional resources: [MinMaxGradient](ParticleSystem.MinMaxGradient.html).

    
    
    using UnityEngine;
    using System.Collections;  
      
    [[RequireComponent](RequireComponent.html)(typeof([ParticleSystem](ParticleSystem.html)))]
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        private [ParticleSystem](ParticleSystem.html) ps;
        private [Gradient](Gradient.html) gradient = new [Gradient](Gradient.html)();
        public bool swapColors = true;  
      
        void Start()
        {
            ps = GetComponent<[ParticleSystem](ParticleSystem.html)>();  
      
            var main = ps.main;
            main.startSize = 0.1f;
            main.startLifetime = 1.5f;  
      
            var trails = ps.trails;
            trails.enabled = true;  
      
            var psr = GetComponent<[ParticleSystemRenderer](ParticleSystemRenderer.html)>();
            psr.trailMaterial = new [Material](Material.html)([Shader.Find](Shader.Find.html)("Sprites/Default"));
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            var trails = ps.trails;
            if (swapColors)
            {
                gradient.SetKeys(
                    new [GradientColorKey](GradientColorKey.html)[] { new [GradientColorKey](GradientColorKey.html)([Color.blue](Color-blue.html), 0.0f), new [GradientColorKey](GradientColorKey.html)([Color.green](Color-green.html), 1.0f) },
                    new [GradientAlphaKey](GradientAlphaKey.html)[] { new [GradientAlphaKey](GradientAlphaKey.html)(1.0f, 0.0f), new [GradientAlphaKey](GradientAlphaKey.html)(1.0f, 1.0f) }
                );
            }
            else
            {
                gradient.SetKeys(
                    new [GradientColorKey](GradientColorKey.html)[] { new [GradientColorKey](GradientColorKey.html)([Color.green](Color-green.html), 0.0f), new [GradientColorKey](GradientColorKey.html)([Color.blue](Color-blue.html), 1.0f) },
                    new [GradientAlphaKey](GradientAlphaKey.html)[] { new [GradientAlphaKey](GradientAlphaKey.html)(1.0f, 0.0f), new [GradientAlphaKey](GradientAlphaKey.html)(1.0f, 1.0f) }
                );
            }  
      
            trails.colorOverTrail = gradient;
        }  
      
        void OnGUI()
        {
            swapColors = [GUI.Toggle](GUI.Toggle.html)(new [Rect](Rect.html)(25, 25, 200, 30), swapColors, "Swap Trail Colors");
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

