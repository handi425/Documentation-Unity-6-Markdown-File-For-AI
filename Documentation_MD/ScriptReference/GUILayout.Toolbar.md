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

#  [GUILayout](GUILayout.html).Toolbar

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

public static int Toolbar(int selected, string[] texts, params
GUILayoutOption[] options);

## Declaration

public static int Toolbar(int selected, Texture[] images, params
GUILayoutOption[] options);

## Declaration

public static int Toolbar(int selected, GUIContent[] contents, params
GUILayoutOption[] options);

## Declaration

public static int Toolbar(int selected, string[] texts,
[GUIStyle](GUIStyle.html) style, params GUILayoutOption[] options);

## Declaration

public static int Toolbar(int selected, Texture[] images,
[GUIStyle](GUIStyle.html) style, params GUILayoutOption[] options);

## Declaration

public static int Toolbar(int selected, GUIContent[] contents,
[GUIStyle](GUIStyle.html) style, params GUILayoutOption[] options);

## Declaration

public static int Toolbar(int selected, string[] texts,
[GUIStyle](GUIStyle.html) style,
[GUI.ToolbarButtonSize](GUI.ToolbarButtonSize.html) buttonSize, params
GUILayoutOption[] options);

## Declaration

public static int Toolbar(int selected, Texture[] images,
[GUIStyle](GUIStyle.html) style,
[GUI.ToolbarButtonSize](GUI.ToolbarButtonSize.html) buttonSize, params
GUILayoutOption[] options);

## Declaration

public static int Toolbar(int selected, GUIContent[] contents,
[GUIStyle](GUIStyle.html) style,
[GUI.ToolbarButtonSize](GUI.ToolbarButtonSize.html) buttonSize, params
GUILayoutOption[] options);

### Parameters

selected | The index of the selected button.  
---|---  
texts | An array of strings to show on the buttons.  
images | An array of textures on the buttons.  
contents | An array of text, image and tooltips for the button.  
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
buttonSize | Determines how toolbar button size is calculated.  
  
### Returns

**int** The index of the selected button.

### Description

Make a toolbar.

![](../StaticFiles/ScriptRefImages/GUILayoutToolbar.png)  
_Toolbar in the Game View._

    
    
    using UnityEngine;  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        int toolbarInt = 0;
        string[] toolbarStrings = {"Toolbar1", "Toolbar2", "Toolbar3"};  
      
        void OnGUI()
        {
            toolbarInt = [GUILayout.Toolbar](GUILayout.Toolbar.html)(toolbarInt, toolbarStrings);
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

