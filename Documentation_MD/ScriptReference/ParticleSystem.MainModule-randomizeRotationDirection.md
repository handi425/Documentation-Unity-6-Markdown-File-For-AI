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

**Method group is Obsolete**  

#
[ParticleSystem.MainModule](ParticleSystem.MainModule.html).randomizeRotationDirection

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

**Obsolete** Please use flipRotation instead.  
**Upgrade to[flipRotation](ParticleSystem.MainModule-flipRotation.html)**
public float randomizeRotationDirection;

### Description

Cause some particles to spin in the opposite direction.

Set between 0 and 1. Higher values cause a higher proportion of particles to
spin in the opposite direction.

    
    
    using UnityEngine;
    using System.Collections;  
      
    [[RequireComponent](RequireComponent.html)(typeof([ParticleSystem](ParticleSystem.html)))]
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        private [ParticleSystem](ParticleSystem.html) ps;
        public float hSliderValue = 0.0F;  
      
        void Start()
        {
            ps = GetComponent<[ParticleSystem](ParticleSystem.html)>();  
      
            var rot = ps.rotationOverLifetime;
            rot.enabled = true;
            rot.zMultiplier = 90.0f * [Mathf.Deg2Rad](Mathf.Deg2Rad.html);  
      
            var psr = GetComponent<[ParticleSystemRenderer](ParticleSystemRenderer.html)>();
            psr.material = new [Material](Material.html)([Shader.Find](Shader.Find.html)("Sprites/Default"));    // this material renders a square billboard, so we can see the rotation
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            var main = ps.main;
            main.randomizeRotationDirection = hSliderValue;
        }  
      
        void OnGUI()
        {
            hSliderValue = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(25, 25, 100, 30), hSliderValue, 0.0F, 1.0F);
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

