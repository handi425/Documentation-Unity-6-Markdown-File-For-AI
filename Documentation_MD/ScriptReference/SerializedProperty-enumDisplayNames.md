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

#  [SerializedProperty](SerializedProperty.html).enumDisplayNames

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

public string[] enumDisplayNames;

### Description

Display-friendly names of enumeration of an enum property.

Similar to enumNames, but formatted with spaces and capitalization.  
  
Additional resources: [enumNames](SerializedProperty-enumNames.html),
[propertyType](SerializedProperty-propertyType.html),
[SerializedPropertyType.Enum](SerializedPropertyType.Enum.html),
[enumValueIndex](SerializedProperty-enumValueIndex.html),
[InspectorNameAttribute](InspectorNameAttribute.html).

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    public enum OptionEnum
    {
        ValueFirst = 1,
        ValueSecond = 2,
        ValueThird = 3,  
      
        [InspectorName("Value 4 - Best choice")]
        ValueForth = 4,  
      
        [InspectorName("Value 5 - Avoid")]
        ValueFifth = 5,  
      
        None = 0
    }  
      
    public class EnumDisplayNameExample : [ScriptableObject](ScriptableObject.html)
    {
        public OptionEnum MyEnum = OptionEnum.ValueForth;  
      
        [[MenuItem](MenuItem.html)("Example/[SerializedProperty](SerializedProperty.html) enumDisplayName Example")]
        static void MenuCallbackup()
        {
            EnumDisplayNameExample obj = [ScriptableObject.CreateInstance](ScriptableObject.CreateInstance.html)<EnumDisplayNameExample>();
            [SerializedObject](SerializedObject.html) serializedObject = new [SerializedObject](SerializedObject.html)(obj);
            [SerializedProperty](SerializedProperty.html) enumProperty = serializedObject.FindProperty("MyEnum");  
      
            // Print the members of the enum, sorted by value
            // Will output:
            // Names: None,ValueFirst,ValueSecond,ValueThird,ValueForth,ValueFifth
            [Debug.Log](Debug.Log.html)("Names: " + string.Join(",", enumProperty.enumNames));  
      
            //The display names show the InspectorName string when specified,
            //otherwise a more human readable version of the enum member name
            //Will output:
            //[Display](Display.html) names: None,Value First,Value Second,Value Third,Value 4 - Best choice,Value 5 - Avoid
            [Debug.Log](Debug.Log.html)("[Display](Display.html) names: " + string.Join(",", enumProperty.enumDisplayNames));  
      
            //Will output:
            //Current value: Value 4 - Best choice
            [Debug.Log](Debug.Log.html)("Current value: " + enumProperty.enumDisplayNames[enumProperty.enumValueIndex]);
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

