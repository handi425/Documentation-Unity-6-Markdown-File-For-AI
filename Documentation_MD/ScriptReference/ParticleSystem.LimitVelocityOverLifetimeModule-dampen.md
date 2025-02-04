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
[ParticleSystem.LimitVelocityOverLifetimeModule](ParticleSystem.LimitVelocityOverLifetimeModule.html).dampen

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

public float dampen;

### Description

Controls how much this module dampens particle velocities that exceed the
velocity limit.

    
    
    using UnityEngine;
    using System.Collections;  
      
    [[RequireComponent](RequireComponent.html)(typeof([ParticleSystem](ParticleSystem.html)))]
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        private [ParticleSystem](ParticleSystem.html) ps;
        public bool moduleEnabled = true;
        public float hSliderValueSpeed = 0.0f;
        public float hSliderValueDampen = 0.1f;  
      
        void Start()
        {
            ps = GetComponent<[ParticleSystem](ParticleSystem.html)>();
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            var limitVelocityOverLifetime = ps.limitVelocityOverLifetime;
            limitVelocityOverLifetime.enabled = moduleEnabled;
            limitVelocityOverLifetime.limitMultiplier = hSliderValueSpeed;
            limitVelocityOverLifetime.dampen = hSliderValueDampen;
        }  
      
        void OnGUI()
        {
            moduleEnabled = [GUI.Toggle](GUI.Toggle.html)(new [Rect](Rect.html)(25, 45, 200, 30), moduleEnabled, "Enabled");  
      
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, 80, 100, 30), "Speed Limit");
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, 120, 100, 30), "Dampen");  
      
            hSliderValueSpeed = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(95, 85, 100, 30), hSliderValueSpeed, 0.0f, 2.0f);
            hSliderValueDampen = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(95, 125, 100, 30), hSliderValueDampen, 0.0f, 1.0f);
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

