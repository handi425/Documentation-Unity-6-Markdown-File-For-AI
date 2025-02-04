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
[ParticleSystem.RotationBySpeedModule](ParticleSystem.RotationBySpeedModule.html).range

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

public [Vector2](Vector2.html) range;

### Description

Set the minimum and maximum speeds that this module applies the rotation curve
between.

Additional resources: ParticleSystem.RotationBySpeedModule.angularVelocity.

    
    
    using UnityEngine;
    using System.Collections;  
      
    [[RequireComponent](RequireComponent.html)(typeof([ParticleSystem](ParticleSystem.html)))]
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        private [ParticleSystem](ParticleSystem.html) ps;
        public float hSliderValue = 1.0f;  
      
        void Start()
        {
            ps = GetComponent<[ParticleSystem](ParticleSystem.html)>();  
      
            var rotationBySpeed = ps.rotationBySpeed;
            rotationBySpeed.enabled = true;  
      
            [AnimationCurve](AnimationCurve.html) curve = new [AnimationCurve](AnimationCurve.html)();
            curve.AddKey(0.0f, 0.0f);
            curve.AddKey(1.0f, 1.0f);  
      
            rotationBySpeed.z = new [ParticleSystem.MinMaxCurve](ParticleSystem.MinMaxCurve.html)(1.0f, curve);
            rotationBySpeed.range = new [Vector2](Vector2.html)(1.0f, 5.0f);  
      
            var psr = GetComponent<[ParticleSystemRenderer](ParticleSystemRenderer.html)>();
            psr.material = new [Material](Material.html)([Shader.Find](Shader.Find.html)("Sprites/Default"));    // this material renders a square billboard, so we can see the rotation
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            var main = ps.main;
            main.startSpeed = hSliderValue;
        }  
      
        void OnGUI()
        {
            hSliderValue = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(25, 45, 100, 30), hSliderValue, 1.0f, 5.0f);
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

