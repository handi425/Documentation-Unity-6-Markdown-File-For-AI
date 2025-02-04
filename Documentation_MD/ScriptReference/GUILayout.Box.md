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

#  [GUILayout](GUILayout.html).Box

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

public static void Box([Texture](Texture.html) image, params GUILayoutOption[]
options);

## Declaration

public static void Box(string text, params GUILayoutOption[] options);

## Declaration

public static void Box([GUIContent](GUIContent.html) content, params
GUILayoutOption[] options);

## Declaration

public static void Box([Texture](Texture.html) image,
[GUIStyle](GUIStyle.html) style, params GUILayoutOption[] options);

## Declaration

public static void Box(string text, [GUIStyle](GUIStyle.html) style, params
GUILayoutOption[] options);

## Declaration

public static void Box([GUIContent](GUIContent.html) content,
[GUIStyle](GUIStyle.html) style, params GUILayoutOption[] options);

### Parameters

text | Text to display on the box.  
---|---  
image |  [Texture](Texture.html) to display on the box.  
content | Text, image and tooltip for this box.  
style | The style to use. If left out, the `box` style from the current [GUISkin](GUISkin.html) is used.  
options | An optional list of layout options that specify extra layouting properties. Any values passed in here will override settings defined by the `style`.  
Additional resources: [GUILayout.Width](GUILayout.Width.html),
[GUILayout.Height](GUILayout.Height.html),
[GUILayout.MinWidth](GUILayout.MinWidth.html),
[GUILayout.MaxWidth](GUILayout.MaxWidth.html),
[GUILayout.MinHeight](GUILayout.MinHeight.html),
[GUILayout.MaxHeight](GUILayout.MaxHeight.html),
[GUILayout.ExpandWidth](GUILayout.ExpandWidth.html),
[GUILayout.ExpandHeight](GUILayout.ExpandHeight.html).  
  
### Description

Make an auto-layout box.

This will make a box that contains static text or images but not other GUI
controls. If you want to make a rectangular container for a set of GUI
controls, use one of the grouping functions
([BeginHorizontal](GUILayout.BeginHorizontal.html),
[BeginVertical](GUILayout.BeginVertical.html),
[BeginArea](GUILayout.BeginArea.html), etc...).  
  
![](../StaticFiles/ScriptRefImages/GUILayoutBox.png)  
_Boxes in the Game View._

    
    
    using UnityEngine;  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        [Texture](Texture.html) tex;  
      
        void OnGUI()
        {
            if (!tex)
            {
                [Debug.LogError](Debug.LogError.html)("Missing texture, assign a texture in the inspector");
            }
            [GUILayout.Box](GUILayout.Box.html)(tex);
            [GUILayout.Box](GUILayout.Box.html)("This is a sized label");
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

