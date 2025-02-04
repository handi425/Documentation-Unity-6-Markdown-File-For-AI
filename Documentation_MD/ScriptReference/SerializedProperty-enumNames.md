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

#  [SerializedProperty](SerializedProperty.html).enumNames

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

public string[] enumNames;

### Description

Names of enumeration of an enum property.

Additional resources: [enumDisplayNames](SerializedProperty-
enumDisplayNames.html), [propertyType](SerializedProperty-propertyType.html),
[SerializedPropertyType.Enum](SerializedPropertyType.Enum.html),
[enumValueIndex](SerializedProperty-enumValueIndex.html).

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    public enum ExampleEnum
    {
        ValueFirst = 1,
        ValueSecond = 2,
        ValueThird = 3,
    }  
      
    public class EnumExample : [ScriptableObject](ScriptableObject.html)
    {
        public ExampleEnum MyEnum = ExampleEnum.ValueSecond;  
      
        [[MenuItem](MenuItem.html)("Example/[SerializedProperty](SerializedProperty.html) Enum API")]
        static void Example()
        {
            EnumExample obj = [ScriptableObject.CreateInstance](ScriptableObject.CreateInstance.html)<EnumExample>();
            [SerializedObject](SerializedObject.html) serializedObject = new [SerializedObject](SerializedObject.html)(obj);
            [SerializedProperty](SerializedProperty.html) enumProperty = serializedObject.FindProperty("MyEnum");  
      
            //MyEnum value: 2
            //Name of current value: ValueSecond
            //DisplayName: Value Second
            [Debug.Log](Debug.Log.html)("MyEnum value: " + enumProperty.intValue +
                "\nName of current value: " + enumProperty.enumNames[enumProperty.enumValueIndex] +
                "\nDisplayName: " + enumProperty.enumDisplayNames[enumProperty.enumValueIndex]);
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

