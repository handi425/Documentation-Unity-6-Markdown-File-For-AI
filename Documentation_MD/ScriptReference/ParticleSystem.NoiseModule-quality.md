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

#  [ParticleSystem.NoiseModule](ParticleSystem.NoiseModule.html).quality

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

public [ParticleSystemNoiseQuality](ParticleSystemNoiseQuality.html) quality;

### Description

Generate 1D, 2D or 3D noise.

    
    
    using UnityEngine;
    using System.Collections;  
      
    [[RequireComponent](RequireComponent.html)(typeof([ParticleSystem](ParticleSystem.html)))]
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        private [ParticleSystem](ParticleSystem.html) ps;
        public bool moduleEnabled = true;
        public float hSliderValueStrength = 1.0f;
        public float hSliderValueFrequency = 1.0f;
        public float hSliderValueScrollSpeed = 0.0f;
        public bool damping = true;
        public [ParticleSystemNoiseQuality](ParticleSystemNoiseQuality.html) quality = [ParticleSystemNoiseQuality.High](ParticleSystemNoiseQuality.High.html);  
      
        void Start()
        {
            ps = GetComponent<[ParticleSystem](ParticleSystem.html)>();  
      
            // Set color by speed, to demonstrate the effects of the Noise Module
            var colorBySpeed = ps.colorBySpeed;
            colorBySpeed.enabled = true;  
      
            [Gradient](Gradient.html) gradient = new [Gradient](Gradient.html)();
            gradient.SetKeys(
                new [GradientColorKey](GradientColorKey.html)[] { new [GradientColorKey](GradientColorKey.html)([Color.green](Color-green.html), 0.0f), new [GradientColorKey](GradientColorKey.html)([Color.red](Color-red.html), 1.0f) },
                new [GradientAlphaKey](GradientAlphaKey.html)[] { new [GradientAlphaKey](GradientAlphaKey.html)(1.0f, 0.0f), new [GradientAlphaKey](GradientAlphaKey.html)(1.0f, 1.0f) }
            );  
      
            colorBySpeed.color = new [ParticleSystem.MinMaxGradient](ParticleSystem.MinMaxGradient.html)(gradient);
            colorBySpeed.range = new [Vector2](Vector2.html)(3.0f, 7.0f);
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            var noise = ps.noise;
            noise.enabled = moduleEnabled;
            noise.strengthMultiplier = hSliderValueStrength;
            noise.frequency = hSliderValueFrequency;
            noise.scrollSpeedMultiplier = hSliderValueScrollSpeed;
            noise.damping = damping;
            noise.quality = quality;
        }  
      
        void OnGUI()
        {
            moduleEnabled = [GUI.Toggle](GUI.Toggle.html)(new [Rect](Rect.html)(25, 45, 200, 30), moduleEnabled, "Enabled");  
      
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, 80, 100, 30), "Strength");
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, 120, 100, 30), "Frequency");
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, 160, 100, 30), "Scroll Speed");  
      
            hSliderValueStrength = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(135, 85, 100, 30), hSliderValueStrength, 0.0f, 5.0f);
            hSliderValueFrequency = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(135, 125, 100, 30), hSliderValueFrequency, 0.0f, 5.0f);
            hSliderValueScrollSpeed = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(135, 165, 100, 30), hSliderValueScrollSpeed, 0.0f, 5.0f);  
      
            damping = [GUI.Toggle](GUI.Toggle.html)(new [Rect](Rect.html)(25, 205, 200, 30), damping, "Damping");  
      
            quality = ([ParticleSystemNoiseQuality](ParticleSystemNoiseQuality.html))[GUI.SelectionGrid](GUI.SelectionGrid.html)(new [Rect](Rect.html)(25, 245, 300, 30), (int)quality, new [GUIContent](GUIContent.html)[] { new [GUIContent](GUIContent.html)("Low"), new [GUIContent](GUIContent.html)("Medium"), new [GUIContent](GUIContent.html)("High") }, 3);
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

