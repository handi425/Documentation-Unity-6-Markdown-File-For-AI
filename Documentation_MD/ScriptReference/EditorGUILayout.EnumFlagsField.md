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

#  [EditorGUILayout](EditorGUILayout.html).EnumFlagsField

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

public static Enum EnumFlagsField(Enum enumValue, params GUILayoutOption[]
options);

## Declaration

public static Enum EnumFlagsField(Enum enumValue, [GUIStyle](GUIStyle.html)
style, params GUILayoutOption[] options);

## Declaration

public static Enum EnumFlagsField(string label, Enum enumValue, params
GUILayoutOption[] options);

## Declaration

public static Enum EnumFlagsField(string label, Enum enumValue,
[GUIStyle](GUIStyle.html) style, params GUILayoutOption[] options);

## Declaration

public static Enum EnumFlagsField([GUIContent](GUIContent.html) label, Enum
enumValue, params GUILayoutOption[] options);

## Declaration

public static Enum EnumFlagsField([GUIContent](GUIContent.html) label, Enum
enumValue, [GUIStyle](GUIStyle.html) style, params GUILayoutOption[] options);

## Declaration

public static Enum EnumFlagsField([GUIContent](GUIContent.html) label, Enum
enumValue, bool includeObsolete, params GUILayoutOption[] options);

## Declaration

public static Enum EnumFlagsField([GUIContent](GUIContent.html) label, Enum
enumValue, bool includeObsolete, [GUIStyle](GUIStyle.html) style, params
GUILayoutOption[] options);

### Parameters

label | Optional label to display in front of the enum flags field.  
---|---  
enumValue | Enum flags value.  
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
  
### Returns

**Enum** The enum flags value modified by the user. This is a selection
BitMask where each bit represents an Enum value index. (Note this returned
value is not itself an Enum).

### Description

Displays a menu with an option for every value of the enum type when clicked.

An option for the value `0` with name "Nothing" and an option for the value
`~0` (that is, all bits set) with the name "Everything" are always displayed
at the top of the menu. The names for the values `0` and `~0` can be overriden
by defining these values in the enum type.  
  
**Note:** This method only supports enums whose underlying types are supported
by Unity's serialization system (sbyte, short, int, byte, ushort, or uint).
For enums backed by an unsigned type, the "Everything" option should have the
value corresponding to all bits set (i.e. `~0` in an unchecked context or the
`MaxValue` constant for the type).  
  
![](../StaticFiles/ScriptRefImages/EditorGUIEnumFlagsField.png)  
_Simple editor window that shows the enum flags field._

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    class EnumFlagsFieldExample : [EditorWindow](EditorWindow.html)
    {
        enum ExampleFlagsEnum
        {
            None = 0, // Custom name for "Nothing" option
            A = 1 << 0,
            B = 1 << 1,
            AB = A | B, // Combination of two flags
            C = 1 << 2,
            All = ~0, // Custom name for "Everything" option
        }  
      
        ExampleFlagsEnum m_Flags;  
      
        [[MenuItem](MenuItem.html)("Examples/[EnumFlagsField](UIElements.EnumFlagsField.html) Example")]
        static void OpenWindow()
        {
            GetWindow<EnumFlagsFieldExample>().Show();
        }  
      
        void OnGUI()
        {
            m_Flags = (ExampleFlagsEnum)[EditorGUILayout.EnumFlagsField](EditorGUILayout.EnumFlagsField.html)(m_Flags);
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

