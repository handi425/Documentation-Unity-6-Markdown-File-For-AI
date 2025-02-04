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

#  [GUILayout](GUILayout.html).Toggle

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

public static bool Toggle(bool value, [Texture](Texture.html) image, params
GUILayoutOption[] options);

## Declaration

public static bool Toggle(bool value, string text, params GUILayoutOption[]
options);

## Declaration

public static bool Toggle(bool value, [GUIContent](GUIContent.html) content,
params GUILayoutOption[] options);

## Declaration

public static bool Toggle(bool value, [Texture](Texture.html) image,
[GUIStyle](GUIStyle.html) style, params GUILayoutOption[] options);

## Declaration

public static bool Toggle(bool value, string text, [GUIStyle](GUIStyle.html)
style, params GUILayoutOption[] options);

## Declaration

public static bool Toggle(bool value, [GUIContent](GUIContent.html) content,
[GUIStyle](GUIStyle.html) style, params GUILayoutOption[] options);

### Parameters

value | Is the button on or off?  
---|---  
text | Text to display on the button.  
image |  [Texture](Texture.html) to display on the button.  
content | Text, image and tooltip for this button.  
style | The style to use. If left out, the `button` style from the current [GUISkin](GUISkin.html) is used.  
options | An optional list of layout options that specify extra layouting properties. Any values passed in here will override settings defined by the `style`.  
Additional resources: [GUILayout.Width](GUILayout.Width.html),
[GUILayout.Height](GUILayout.Height.html),
[GUILayout.MinWidth](GUILayout.MinWidth.html),
[GUILayout.MaxWidth](GUILayout.MaxWidth.html),
[GUILayout.MinHeight](GUILayout.MinHeight.html),
[GUILayout.MaxHeight](GUILayout.MaxHeight.html),
[GUILayout.ExpandWidth](GUILayout.ExpandWidth.html),
[GUILayout.ExpandHeight](GUILayout.ExpandHeight.html).  
  
### Returns

**bool** The new value of the button.

### Description

Make an on/off toggle button.

![](../StaticFiles/ScriptRefImages/GUILayoutToggle.png)  
_Toggle button in the Game View._

    
    
    using UnityEngine;  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        // Draws 2 toggle controls, one with a text, the other with an image.
        [Texture](Texture.html) aTexture;  
      
        bool toggleTxt = false;
        bool toggleImg = false;  
      
        void OnGUI()
        {
            if (!aTexture)
            {
                [Debug.LogError](Debug.LogError.html)("Please assign a texture in the inspector.");
                return;
            }
            toggleTxt = [GUILayout.Toggle](GUILayout.Toggle.html)(toggleTxt, "A [Toggle](UIElements.Toggle.html) text");
            toggleImg = [GUILayout.Toggle](GUILayout.Toggle.html)(toggleImg, aTexture);
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

