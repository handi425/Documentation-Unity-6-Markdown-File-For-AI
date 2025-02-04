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

#  [TrailRenderer](TrailRenderer.html).widthCurve

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

[Switch to Manual](../Manual/class-TrailRenderer.html "Go to TrailRenderer
Component in the Manual")

public [AnimationCurve](AnimationCurve.html) widthCurve;

### Description

Set the curve describing the width of the trail at various points along its
length.

This property is multiplied by [TrailRenderer.widthMultiplier](TrailRenderer-
widthMultiplier.html) to get the final width of the trail.

    
    
    using UnityEngine;
    using System.Collections;  
      
    [[RequireComponent](RequireComponent.html)(typeof([TrailRenderer](TrailRenderer.html)))]
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public float width = 1.0f;
        public bool useCurve = true;
        private [TrailRenderer](TrailRenderer.html) tr;  
      
        void Start()
        {
            tr = GetComponent<[TrailRenderer](TrailRenderer.html)>();
            tr.material = new [Material](Material.html)([Shader.Find](Shader.Find.html)("Sprites/Default"));
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            [AnimationCurve](AnimationCurve.html) curve = new [AnimationCurve](AnimationCurve.html)();
            if (useCurve)
            {
                curve.AddKey(0.0f, 0.0f);
                curve.AddKey(1.0f, 1.0f);
            }
            else
            {
                curve.AddKey(0.0f, 1.0f);
                curve.AddKey(1.0f, 1.0f);
            }  
      
            tr.widthCurve = curve;
            tr.widthMultiplier = width;
            tr.transform.position = new [Vector3](Vector3.html)([Mathf.Sin](Mathf.Sin.html)([Time.time](Time-time.html) * 1.51f) * 7.0f, [Mathf.Cos](Mathf.Cos.html)([Time.time](Time-time.html) * 1.27f) * 4.0f, 0.0f);
        }  
      
        void OnGUI()
        {
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, 20, 200, 30), "Width");
            width = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(125, 25, 200, 30), width, 0.1f, 1.0f);
            useCurve = [GUI.Toggle](GUI.Toggle.html)(new [Rect](Rect.html)(25, 65, 200, 30), useCurve, "Use Curve");
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

