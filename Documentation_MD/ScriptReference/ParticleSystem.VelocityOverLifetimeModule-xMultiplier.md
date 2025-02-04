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
[ParticleSystem.VelocityOverLifetimeModule](ParticleSystem.VelocityOverLifetimeModule.html).xMultiplier

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

public float xMultiplier;

### Description

A multiplier for
[ParticleSystem.VelocityOverLifetimeModule.x](ParticleSystem.VelocityOverLifetimeModule-x.html)

Changing this property is more efficient than accessing the entire curve, if
you only want to change the overall speed multiplier.

    
    
    using UnityEngine;
    using System.Collections;  
      
    [[RequireComponent](RequireComponent.html)(typeof([ParticleSystem](ParticleSystem.html)))]
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        private [ParticleSystem](ParticleSystem.html) ps;
        public float hSliderValueX = 1.0f;
        public float hSliderValueY = 1.0f;
        public float hSliderValueZ = 1.0f;  
      
        void Start()
        {
            ps = GetComponent<[ParticleSystem](ParticleSystem.html)>();  
      
            var velocityOverLifetime = ps.velocityOverLifetime;
            velocityOverLifetime.enabled = true;
            velocityOverLifetime.space = [ParticleSystemSimulationSpace.World](ParticleSystemSimulationSpace.World.html);  
      
            [AnimationCurve](AnimationCurve.html) curve = new [AnimationCurve](AnimationCurve.html)();
            curve.AddKey(0.0f, 0.0f);
            curve.AddKey(1.0f, 1.0f);  
      
            [ParticleSystem.MinMaxCurve](ParticleSystem.MinMaxCurve.html) minMaxCurve = new [ParticleSystem.MinMaxCurve](ParticleSystem.MinMaxCurve.html)(1.0f, curve);  
      
            velocityOverLifetime.x = minMaxCurve;
            velocityOverLifetime.y = minMaxCurve;
            velocityOverLifetime.z = minMaxCurve;
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            var velocityOverLifetime = ps.velocityOverLifetime;
            velocityOverLifetime.xMultiplier = hSliderValueX;
            velocityOverLifetime.yMultiplier = hSliderValueY;
            velocityOverLifetime.zMultiplier = hSliderValueZ;
        }  
      
        void OnGUI()
        {
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, 40, 100, 30), "X");
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, 80, 100, 30), "Y");
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, 120, 100, 30), "Z");  
      
            hSliderValueX = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(55, 45, 100, 30), hSliderValueX, -50.0f, 50.0f);
            hSliderValueY = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(55, 85, 100, 30), hSliderValueY, -50.0f, 50.0f);
            hSliderValueZ = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(55, 125, 100, 30), hSliderValueZ, -50.0f, 50.0f);
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

