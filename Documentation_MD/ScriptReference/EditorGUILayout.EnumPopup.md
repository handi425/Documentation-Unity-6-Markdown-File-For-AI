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

#  [EditorGUILayout](EditorGUILayout.html).EnumPopup

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

public static Enum EnumPopup(Enum selected, params GUILayoutOption[] options);

## Declaration

public static Enum EnumPopup(Enum selected, [GUIStyle](GUIStyle.html) style,
params GUILayoutOption[] options);

## Declaration

public static Enum EnumPopup(string label, Enum selected, params
GUILayoutOption[] options);

## Declaration

public static Enum EnumPopup(string label, Enum selected,
[GUIStyle](GUIStyle.html) style, params GUILayoutOption[] options);

## Declaration

public static Enum EnumPopup([GUIContent](GUIContent.html) label, Enum
selected, params GUILayoutOption[] options);

## Declaration

public static Enum EnumPopup([GUIContent](GUIContent.html) label, Enum
selected, [GUIStyle](GUIStyle.html) style, params GUILayoutOption[] options);

## Declaration

public static Enum EnumPopup([GUIContent](GUIContent.html) label, Enum
selected, Func<Enum,bool> checkEnabled, bool includeObsolete, params
GUILayoutOption[] options);

## Declaration

public static Enum EnumPopup([GUIContent](GUIContent.html) label, Enum
selected, Func<Enum,bool> checkEnabled, bool includeObsolete,
[GUIStyle](GUIStyle.html) style, params GUILayoutOption[] options);

### Parameters

label | Optional label in front of the field.  
---|---  
selected | The enum option the field shows.  
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
includeObsolete | Set to true to include Enum values with ObsoleteAttribute. Set to false to exclude Enum values with ObsoleteAttribute.  
checkEnabled | Method called for each Enum value displayed. The specified method should return true if the option can be selected, false otherwise.  
  
### Returns

**Enum** The enum option that has been selected by the user.

### Description

Make an enum popup selection field.

Takes the currently selected enum value as a parameter and returns the enum
value selected by the user.  
  
![](../StaticFiles/ScriptRefImages/EditorGUILayoutEnumPopup.png)  
_Creates a primitive selected by the user._

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;
    using System.Collections;  
      
    // Creates an instance of a primitive depending on the option selected by the user.  
      
    public enum OPTIONS
    {
        CUBE = 0,
        SPHERE = 1,
        PLANE = 2
    }  
      
    public class EditorGUILayoutEnumPopup : [EditorWindow](EditorWindow.html)
    {
        public OPTIONS op;
        [[MenuItem](MenuItem.html)("Examples/[Editor](Editor.html) [GUILayout](GUILayout.html) Enum Popup usage")]
        static void Init()
        {
            UnityEditor.EditorWindow window = GetWindow(typeof(EditorGUILayoutEnumPopup));
            window.Show();
        }  
      
        void OnGUI()
        {
            op = (OPTIONS)[EditorGUILayout.EnumPopup](EditorGUILayout.EnumPopup.html)("Primitive to create:", op);
            if ([GUILayout.Button](GUILayout.Button.html)("Create"))
                InstantiatePrimitive(op);
        }  
      
        void InstantiatePrimitive(OPTIONS op)
        {
            switch (op)
            {
                case OPTIONS.CUBE:
                    [GameObject](GameObject.html) cube = [GameObject.CreatePrimitive](GameObject.CreatePrimitive.html)([PrimitiveType.Cube](PrimitiveType.Cube.html));
                    cube.transform.position = [Vector3.zero](Vector3-zero.html);
                    break;
                case OPTIONS.SPHERE:
                    [GameObject](GameObject.html) sphere = [GameObject.CreatePrimitive](GameObject.CreatePrimitive.html)([PrimitiveType.Sphere](PrimitiveType.Sphere.html));
                    sphere.transform.position = [Vector3.zero](Vector3-zero.html);
                    break;
                case OPTIONS.PLANE:
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

