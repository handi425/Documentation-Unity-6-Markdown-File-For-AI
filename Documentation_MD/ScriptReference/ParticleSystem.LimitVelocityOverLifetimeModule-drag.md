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
[ParticleSystem.LimitVelocityOverLifetimeModule](ParticleSystem.LimitVelocityOverLifetimeModule.html).drag

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

public [ParticleSystem.MinMaxCurve](ParticleSystem.MinMaxCurve.html) drag;

### Description

Controls the amount of drag that this modules applies to the particle
velocities.

Additional resources:
[ParticleSystem.LimitVelocityOverLifetimeModule.multiplyDragByParticleSize](ParticleSystem.LimitVelocityOverLifetimeModule-
multiplyDragByParticleSize.html),
[ParticleSystem.LimitVelocityOverLifetimeModule.multiplyDragByParticleVelocity](ParticleSystem.LimitVelocityOverLifetimeModule-
multiplyDragByParticleVelocity.html).

    
    
    using UnityEngine;
    using System.Collections;  
      
    [[RequireComponent](RequireComponent.html)(typeof([ParticleSystem](ParticleSystem.html)))]
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        private [ParticleSystem](ParticleSystem.html) ps;
        public float hSliderValueDrag = 1.0f;
        public bool hToggleUseSize = false;
        public bool hToggleUseVelocity = false;  
      
        void Start()
        {
            ps = GetComponent<[ParticleSystem](ParticleSystem.html)>();  
      
            var limitVelocityOverLifetime = ps.limitVelocityOverLifetime;
            limitVelocityOverLifetime.enabled = true;  
      
            var main = ps.main;
            main.startSize = new [ParticleSystem.MinMaxCurve](ParticleSystem.MinMaxCurve.html)(0.1f, 1.5f);
            main.startSpeed = new [ParticleSystem.MinMaxCurve](ParticleSystem.MinMaxCurve.html)(0.5f, 5.0f);
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            var limitVelocityOverLifetime = ps.limitVelocityOverLifetime;
            limitVelocityOverLifetime.drag = hSliderValueDrag;
            limitVelocityOverLifetime.multiplyDragByParticleSize = hToggleUseSize;
            limitVelocityOverLifetime.multiplyDragByParticleVelocity = hToggleUseVelocity;
        }  
      
        void OnGUI()
        {
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, 40, 100, 30), "Drag");  
      
            hSliderValueDrag = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(135, 45, 100, 30), hSliderValueDrag, 0.0f, 3.0f);
            hToggleUseSize = [GUI.Toggle](GUI.Toggle.html)(new [Rect](Rect.html)(25, 85, 200, 30), hToggleUseSize, "Multiply by Size");
            hToggleUseVelocity = [GUI.Toggle](GUI.Toggle.html)(new [Rect](Rect.html)(25, 125, 200, 30), hToggleUseVelocity, "Multiply by Velocity");
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

