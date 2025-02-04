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

#  [ParticleSystem.MainModule](ParticleSystem.MainModule.html).startColor

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
startColor;

### Description

The initial color of particles when the Particle System first spawns them.

Additional resources: [MinMaxGradient](ParticleSystem.MinMaxGradient.html).

    
    
    using UnityEngine;
    using System.Collections;  
      
    [[RequireComponent](RequireComponent.html)(typeof([ParticleSystem](ParticleSystem.html)))]
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        private [ParticleSystem](ParticleSystem.html) ps;
        public float hSliderValueR = 0.0F;
        public float hSliderValueG = 0.0F;
        public float hSliderValueB = 0.0F;
        public float hSliderValueA = 1.0F;  
      
        void Start()
        {
            ps = GetComponent<[ParticleSystem](ParticleSystem.html)>();
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            var main = ps.main;
            main.startColor = new [Color](Color.html)(hSliderValueR, hSliderValueG, hSliderValueB, hSliderValueA);
        }  
      
        void OnGUI()
        {
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, 40, 100, 30), "Red");
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, 70, 100, 30), "Green");
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, 100, 100, 30), "Blue");
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, 130, 100, 30), "Alpha");  
      
            hSliderValueR = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(95, 45, 100, 30), hSliderValueR, 0.0F, 1.0F);
            hSliderValueG = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(95, 75, 100, 30), hSliderValueG, 0.0F, 1.0F);
            hSliderValueB = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(95, 105, 100, 30), hSliderValueB, 0.0F, 1.0F);
            hSliderValueA = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(95, 135, 100, 30), hSliderValueA, 0.0F, 1.0F);
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

