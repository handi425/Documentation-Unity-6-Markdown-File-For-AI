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

#  [SphericalHarmonicsL2](Rendering.SphericalHarmonicsL2.html).Evaluate

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

[ ]()

## Declaration

public void Evaluate(Vector3[] directions, Color[] results);

### Parameters

directions | Array of normalized directions in which to evaluate the spherical harmonics.  
---|---  
results | Output array for the evaluated values. The order of the results is the same as the directions array.  
  
### Description

Evaluates the spherical harmonics for each given direction. The `directions`
and `results` arrays must have the same size.

    
    
    using System.Collections;
    using UnityEngine;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            UnityEngine.Rendering.SphericalHarmonicsL2 sh2;
            [LightProbes.GetInterpolatedProbe](LightProbes.GetInterpolatedProbe.html)(new [Vector3](Vector3.html)(0.0f, 0.0f, 0.0f), null, out sh2);  
      
            [Vector3](Vector3.html)[] directions = new [Vector3](Vector3.html)[]
            {
                new [Vector3](Vector3.html)(0.0f, 1.0f, 0.0f),
                new [Vector3](Vector3.html)(0.0f, -1.0f, 0.0f)
            };
            [Color](Color.html)[] results = new [Color](Color.html)[2];  
      
            sh2.Evaluate(directions, results);
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

