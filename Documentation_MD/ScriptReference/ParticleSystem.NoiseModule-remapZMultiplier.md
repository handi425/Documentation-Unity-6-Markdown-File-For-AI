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
[ParticleSystem.NoiseModule](ParticleSystem.NoiseModule.html).remapZMultiplier

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

public float remapZMultiplier;

### Description

z-axis remap multiplier.

Changing this property is more efficient than accessing the entire curve, if
you only want to change the overall remap multiplier. Additional resources:
[ParticleSystem.NoiseModule.remapZ](ParticleSystem.NoiseModule-remapZ.html).

    
    
    using UnityEngine;
    using System.Collections;  
      
    [[RequireComponent](RequireComponent.html)(typeof([ParticleSystem](ParticleSystem.html)))]
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        private [ParticleSystem](ParticleSystem.html) ps;
        public float hSliderValueRemapX = 1.0f;
        public float hSliderValueRemapY = 1.0f;
        public float hSliderValueRemapZ = 1.0f;  
      
        void Start()
        {
            ps = GetComponent<[ParticleSystem](ParticleSystem.html)>();  
      
            var noise = ps.noise;
            noise.enabled = true;
            noise.remapEnabled = true;
            noise.separateAxes = true;  
      
            // An unusual curve to show off different noise behavior (See curve preview in the Inspector)
            [AnimationCurve](AnimationCurve.html) ourCurve;
            ourCurve = new [AnimationCurve](AnimationCurve.html)();
            ourCurve.AddKey(0.0f, 0.0f);
            ourCurve.AddKey(0.45f, -0.75f);
            ourCurve.AddKey(0.50f, 1.0f);
            ourCurve.AddKey(0.55f, -0.75f);
            ourCurve.AddKey(1.0f, 0.0f);  
      
            // Apply the curve
            noise.remapX = new [ParticleSystem.MinMaxCurve](ParticleSystem.MinMaxCurve.html)(1.0f, ourCurve);
            noise.remapY = new [ParticleSystem.MinMaxCurve](ParticleSystem.MinMaxCurve.html)(1.0f, ourCurve);
            noise.remapZ = new [ParticleSystem.MinMaxCurve](ParticleSystem.MinMaxCurve.html)(1.0f, ourCurve);  
      
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
            noise.remapXMultiplier = hSliderValueRemapX;
            noise.remapYMultiplier = hSliderValueRemapY;
            noise.remapZMultiplier = hSliderValueRemapZ;
        }  
      
        void OnGUI()
        {
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, 40, 100, 30), "Remap X");
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, 80, 100, 30), "Remap Y");
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, 120, 100, 30), "Remap Z");  
      
            hSliderValueRemapX = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(135, 45, 100, 30), hSliderValueRemapX, 0.0f, 5.0f);
            hSliderValueRemapY = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(135, 85, 100, 30), hSliderValueRemapY, 0.0f, 5.0f);
            hSliderValueRemapZ = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(135, 125, 100, 30), hSliderValueRemapZ, 0.0f, 5.0f);
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

