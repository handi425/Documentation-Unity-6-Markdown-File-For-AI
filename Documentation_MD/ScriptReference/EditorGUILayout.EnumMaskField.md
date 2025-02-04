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

**Method group is Obsolete**  

#  [EditorGUILayout](EditorGUILayout.html).EnumMaskField

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

**Obsolete** EnumMaskField has been deprecated. Use EnumFlagsField instead.

## Declaration

public static Enum EnumMaskField([GUIContent](GUIContent.html) label, Enum
enumValue, [GUIStyle](GUIStyle.html) style, params GUILayoutOption[] options);

**Obsolete** EnumMaskField has been deprecated. Use EnumFlagsField instead.

## Declaration

public static Enum EnumMaskField(string label, Enum enumValue,
[GUIStyle](GUIStyle.html) style, params GUILayoutOption[] options);

**Obsolete** EnumMaskField has been deprecated. Use EnumFlagsField instead.

## Declaration

public static Enum EnumMaskField([GUIContent](GUIContent.html) label, Enum
enumValue, params GUILayoutOption[] options);

**Obsolete** EnumMaskField has been deprecated. Use EnumFlagsField instead.

## Declaration

public static Enum EnumMaskField(string label, Enum enumValue, params
GUILayoutOption[] options);

**Obsolete** EnumMaskField has been deprecated. Use EnumFlagsField instead.

## Declaration

public static Enum EnumMaskField(Enum enumValue, [GUIStyle](GUIStyle.html)
style, params GUILayoutOption[] options);

**Obsolete** EnumMaskField has been deprecated. Use EnumFlagsField instead.

## Declaration

public static Enum EnumMaskField(Enum enumValue, params GUILayoutOption[]
options);

### Parameters

label | Prefix label for this field.  
---|---  
enumValue | Enum to use for the flags.  
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

**Enum** The value modified by the user.

### Description

This method is obsolete. Use
[EditorGUILayout.EnumFlagsField](EditorGUILayout.EnumFlagsField.html) instead.  
  
Make a field for enum based masks.

Additional resources:
[EditorGUILayout.EnumFlagsField](EditorGUILayout.EnumFlagsField.html).  
  
![](../StaticFiles/ScriptRefImages/MaskField.png)  
_Simple window that shows the enum mask field._ Here is an example of how to
implement an EnumMaskField, giving three options:

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class EditorEnumExample : [EditorWindow](EditorWindow.html)
    {
        public enum Example
        {
            Option_One = 1, //bits: 0000 0001
            Option_Two = 2,  //bits: 0000 0010
            Option_Three = 4     //bits: 0000 0100
        }  
      
        Example   staticFlagMask = 0;  
      
    
        [[MenuItem](MenuItem.html)("Examples/Mask Field Usage")]
        static void Init()
        {
            // Get existing open window or if none, make a new one:
            EditorEnumExample window = (EditorEnumExample)[EditorWindow.GetWindow](EditorWindow.GetWindow.html)(typeof(EditorEnumExample));
            window.Show();
        }  
      
        void OnGUI()
        {
            staticFlagMask = (Example)EditorGUILayout.EnumMaskField("Static [Flags](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.Flags.html)", staticFlagMask);
        }
    }
    

Internally, Unity stores the enum as an int, with each value as a bitmask.
Selecting "Nothing" clears all bits, resulting in an integer value of 0;
selecting "Everything" will set all bits, producing an integer value of -1.  
  
To determine whether a particular enum value has been set, you can either
treat the enum as an int and perform a bitwise OR to test, or you can unset
the "Everything" value by iterating through the enum values and reconstructing
the enum accordingly. An example of how to do this is shown below:

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class EditorEnumExample : [EditorWindow](EditorWindow.html)
    {
        public enum Example
        {
            Option_One = 1, //bits: 0000 0001
            Option_Two = 2,  //bits: 0000 0010
            Option_Three = 4     //bits: 0000 0100
        }  
      
        Example   staticFlagMask = 0;  
      
    
        [[MenuItem](MenuItem.html)("Examples/Mask Field Usage")]
        static void Init()
        {
            // Get existing open window or if none, make a new one:
            EditorEnumExample window = (EditorEnumExample)[EditorWindow.GetWindow](EditorWindow.GetWindow.html)(typeof(EditorEnumExample));
            window.Show();
        }  
      
        void OnGUI()
        {
            staticFlagMask = (Example)EditorGUILayout.EnumMaskField("Static [Flags](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.Flags.html)", staticFlagMask);  
      
            // If "Everything" is set, force Unity to unset the extra bits by iterating through them
            if ((int)staticFlagMask < 0)
            {
                int bits = 0;
                foreach (var enumValue in System.Enum.GetValues(typeof(Example)))
                {
                    int checkBit = (int)staticFlagMask & (int)enumValue;
                    if (checkBit != 0)
                        bits |= (int)enumValue;
                }  
      
                staticFlagMask = (Example)bits;
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

