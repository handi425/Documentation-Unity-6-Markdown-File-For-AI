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

#  [EditorGUILayout](EditorGUILayout.html).Popup

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

public static int Popup(int selectedIndex, string[] displayedOptions, params
GUILayoutOption[] options);

## Declaration

public static int Popup(int selectedIndex, string[] displayedOptions,
[GUIStyle](GUIStyle.html) style, params GUILayoutOption[] options);

## Declaration

public static int Popup(int selectedIndex, GUIContent[] displayedOptions,
params GUILayoutOption[] options);

## Declaration

public static int Popup(int selectedIndex, GUIContent[] displayedOptions,
[GUIStyle](GUIStyle.html) style, params GUILayoutOption[] options);

## Declaration

public static int Popup(string label, int selectedIndex, string[]
displayedOptions, params GUILayoutOption[] options);

## Declaration

public static int Popup(string label, int selectedIndex, string[]
displayedOptions, [GUIStyle](GUIStyle.html) style, params GUILayoutOption[]
options);

## Declaration

public static int Popup([GUIContent](GUIContent.html) label, int
selectedIndex, GUIContent[] displayedOptions, params GUILayoutOption[]
options);

## Declaration

public static int Popup([GUIContent](GUIContent.html) label, int
selectedIndex, GUIContent[] displayedOptions, [GUIStyle](GUIStyle.html) style,
params GUILayoutOption[] options);

### Parameters

label | Optional label in front of the field.  
---|---  
selectedIndex | The index of the option the field shows.  
displayedOptions | An array with the options shown in the popup. Use a slash to separate sub-items (ex. Menu/SubMenu). Use null or an empty string to add a separator. "  
style | Optional [GUIStyle](GUIStyle.html).  
options | An optional list of layout options that specify extra layout properties. Any values passed in here will override settings defined by the `style`.  
Additional resources: [GUILayout.Width](GUILayout.Width.html),
[GUILayout.Height](GUILayout.Height.html),
[GUILayout.MinWidth](GUILayout.MinWidth.html),
[GUILayout.MaxWidth](GUILayout.MaxWidth.html),
[GUILayout.MinHeight](GUILayout.MinHeight.html),
[GUILayout.MaxHeight](GUILayout.MaxHeight.html),
[GUILayout.ExpandWidth](GUILayout.ExpandWidth.html),
[GUILayout.ExpandHeight](GUILayout.ExpandHeight.html).  
  
### Returns

**int** The index of the option that has been selected by the user.

### Description

Make a generic popup selection field.

Takes the currently selected index as a parameter and returns the index
selected by the user.  
  
![](../StaticFiles/ScriptRefImages/EditorGUILayoutPopup.png)  
_Create a primitive depending on the option selected._

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;
    using System.Collections;  
      
    // Creates an instance of a primitive depending on the option selected by the user.
    public class EditorGUILayoutPopup : [EditorWindow](EditorWindow.html)
    {
        public string[] options = new string[] {"Cube", "Sphere", "[Plane](Plane.html)"};
        public int index = 0;
        [[MenuItem](MenuItem.html)("Examples/[Editor](Editor.html) [GUILayout](GUILayout.html) Popup usage")]
        static void Init()
        {
            [EditorWindow](EditorWindow.html) window = GetWindow(typeof(EditorGUILayoutPopup));
            window.Show();
        }  
      
        void OnGUI()
        {
            index = [EditorGUILayout.Popup](EditorGUILayout.Popup.html)(index, options);
            if ([GUILayout.Button](GUILayout.Button.html)("Create"))
                InstantiatePrimitive();
        }  
      
        void InstantiatePrimitive()
        {
            switch (index)
            {
                case 0:
                    [GameObject](GameObject.html) cube = [GameObject.CreatePrimitive](GameObject.CreatePrimitive.html)([PrimitiveType.Cube](PrimitiveType.Cube.html));
                    cube.transform.position = [Vector3.zero](Vector3-zero.html);
                    break;
                case 1:
                    [GameObject](GameObject.html) sphere = [GameObject.CreatePrimitive](GameObject.CreatePrimitive.html)([PrimitiveType.Sphere](PrimitiveType.Sphere.html));
                    sphere.transform.position = [Vector3.zero](Vector3-zero.html);
                    break;
                case 2:
                    [GameObject](GameObject.html) plane = [GameObject.CreatePrimitive](GameObject.CreatePrimitive.html)([PrimitiveType.Plane](PrimitiveType.Plane.html));
                    plane.transform.position = [Vector3.zero](Vector3-zero.html);
                    break;
                default:
                    [Debug.LogError](Debug.LogError.html)("Unrecognized Option");
                    break;
            }
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

