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

#  [SerializedProperty](SerializedProperty.html).EqualContents

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

public static bool EqualContents([SerializedProperty](SerializedProperty.html)
x, [SerializedProperty](SerializedProperty.html) y);

### Description

See if contained serialized properties are equal.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    public class EqualContentsExample : [ScriptableObject](ScriptableObject.html)
    {
        public int m_A = 4;
        public int m_B = 4;  
      
        [[MenuItem](MenuItem.html)("Example/[SerializedProperty](SerializedProperty.html) EqualContents Example")]
        static void Example()
        {
            EqualContentsExample obj = [ScriptableObject.CreateInstance](ScriptableObject.CreateInstance.html)<EqualContentsExample>();
            [SerializedObject](SerializedObject.html) serializedObject = new [SerializedObject](SerializedObject.html)(obj);  
      
            [SerializedProperty](SerializedProperty.html) propertyA = serializedObject.FindProperty("m_A");
            [SerializedProperty](SerializedProperty.html) propertyB = serializedObject.FindProperty("m_B");  
      
            // False because pointing to different properties
            [Debug.Log](Debug.Log.html)("EqualContents : " + [SerializedProperty.EqualContents](SerializedProperty.EqualContents.html)(propertyA, propertyB));  
      
            // True because both have value 4
            [Debug.Log](Debug.Log.html)("DataEquals : " + [SerializedProperty.DataEquals](SerializedProperty.DataEquals.html)(propertyA, propertyB));
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

