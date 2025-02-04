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

#  [Random](Random.html).ColorHSV

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

[Switch to Manual](../Manual/class-random.html "Go to Random Component in the
Manual")

## Declaration

public static [Color](Color.html) ColorHSV();

## Declaration

public static [Color](Color.html) ColorHSV(float hueMin, float hueMax);

## Declaration

public static [Color](Color.html) ColorHSV(float hueMin, float hueMax, float
saturationMin, float saturationMax);

## Declaration

public static [Color](Color.html) ColorHSV(float hueMin, float hueMax, float
saturationMin, float saturationMax, float valueMin, float valueMax);

## Declaration

public static [Color](Color.html) ColorHSV(float hueMin, float hueMax, float
saturationMin, float saturationMax, float valueMin, float valueMax, float
alphaMin, float alphaMax);

### Parameters

hueMin | Minimum hue [0..1].  
---|---  
hueMax | Maximum hue [0..1].  
saturationMin | Minimum saturation [0..1].  
saturationMax | Maximum saturation [0..1].  
valueMin | Minimum value [0..1].  
valueMax | Maximum value [0..1].  
alphaMin | Minimum alpha [0..1].  
alphaMax | Maximum alpha [0..1].  
  
### Returns

**Color** A random color with HSV and alpha values in the (inclusive) input
ranges. Values for each component are derived via linear interpolation of
[value](Random-value.html).

### Description

Generates a random color from HSV and alpha ranges.

    
    
    using UnityEngine;  
      
    public class ColorOnClick : [MonoBehaviour](MonoBehaviour.html)
    {
        void OnMouseDown()
        {
            // Pick a random, saturated and not-too-dark color
            GetComponent<[Renderer](Renderer.html)>().material.color = [Random.ColorHSV](Random.ColorHSV.html)(0f, 1f, 1f, 1f, 0.5f, 1f);
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

