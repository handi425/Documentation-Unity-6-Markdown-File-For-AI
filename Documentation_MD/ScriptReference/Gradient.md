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

# Gradient

class in UnityEngine

/

Implemented in:[UnityEngine.CoreModule](UnityEngine.CoreModule.html)

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

### Description

Represents a Gradient used for animating colors.

Gradients allow animating or interpolating colors by having several "color
keys" and "alpha keys". Color keys and alpha keys are separate, and each key
has a time specified for it, ranging from 0.0 (0%) to 1.0 (100%). Note that
the alpha and colors keys will be automatically sorted by time value and that
it is ensured to always have a minimum of 2 color keys and 2 alpha keys.  
  
How the colors are interpolated between the keys is controlled by
[GradientMode](GradientMode.html).  
  
Public Gradient variables used in scripts automatically display the gradient
editor in the inspector window.
[GradientUsageAttribute](GradientUsageAttribute.html) allows specifying
whether the gradient colors should be high dynamic range for editing.

    
    
    using UnityEngine;  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            var gradient = new [Gradient](Gradient.html)();  
      
            // Blend color from red at 0% to blue at 100%
            var colors = new [GradientColorKey](GradientColorKey.html)[2];
            colors[0] = new [GradientColorKey](GradientColorKey.html)([Color.red](Color-red.html), 0.0f);
            colors[1] = new [GradientColorKey](GradientColorKey.html)([Color.blue](Color-blue.html), 1.0f);  
      
            // Blend alpha from opaque at 0% to transparent at 100%
            var alphas = new [GradientAlphaKey](GradientAlphaKey.html)[2];
            alphas[0] = new [GradientAlphaKey](GradientAlphaKey.html)(1.0f, 0.0f);
            alphas[1] = new [GradientAlphaKey](GradientAlphaKey.html)(0.0f, 1.0f);  
      
            gradient.SetKeys(colors, alphas);  
      
            // What's the color at the relative time 0.25 (25%) ?
            [Debug.Log](Debug.Log.html)(gradient.Evaluate(0.25f));
        }
    }
    

Additional resources: [GradientColorKey](GradientColorKey.html),
[GradientAlphaKey](GradientAlphaKey.html),
[SerializedProperty.gradientValue](SerializedProperty-gradientValue.html).

### Properties

[alphaKeys](Gradient-alphaKeys.html)| All alpha keys defined in the gradient.  
---|---  
[colorKeys](Gradient-colorKeys.html)| All color keys defined in the gradient.  
[colorSpace](Gradient-colorSpace.html)| Indicates the color space that the
gradient color keys are using.  
[mode](Gradient-mode.html)| Controls how the gradient colors are interpolated.  
  
### Constructors

[Gradient](Gradient-ctor.html)| Create a new Gradient object.  
---|---  
  
### Public Methods

[Evaluate](Gradient.Evaluate.html)| Calculate color at a given time.  
---|---  
[SetKeys](Gradient.SetKeys.html)| Setup Gradient with an array of color keys
and alpha keys.  
  
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

