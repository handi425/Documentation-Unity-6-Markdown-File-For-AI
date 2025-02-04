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

#  [SerializedProperty](SerializedProperty.html).arrayElementType

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

public string arrayElementType;

### Description

Type name of the element in an array property. (Read Only)

Returns the C# type name of the element in an array property. In the case of
[SerializedPropertyType.ObjectReference](SerializedPropertyType.ObjectReference.html)
and other internal values of SerializedPropertyType, the internal
serialization type name is returned.

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using System.Collections.Generic;
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class SerializePropertyArrayElementTypeExample : [ScriptableObject](ScriptableObject.html)
    {
        // Various kinds of lists/arrays
        public List<string> m_strings;
        public int[] m_ints;
        public List<[Vector3](Vector3.html)> m_vectors;
        public [GameObject](GameObject.html)[] m_gameObjects;  
      
        [[MenuItem](MenuItem.html)("Example/[SerializedProperty](SerializedProperty.html) arrayElementType Example")]
        static void ArrayElementTypeExample()
        {
            var scriptableObject = [ScriptableObject.CreateInstance](ScriptableObject.CreateInstance.html)<SerializePropertyArrayElementTypeExample>();  
      
            using (var serializedObject = new [SerializedObject](SerializedObject.html)(scriptableObject))
            {
                [LogType](LogType.html)(serializedObject, "m_strings");
                [LogType](LogType.html)(serializedObject, "m_ints");
                [LogType](LogType.html)(serializedObject, "m_vectors");
                [LogType](LogType.html)(serializedObject, "m_gameObjects");
            }
        }  
      
        static void [LogType](LogType.html)([SerializedObject](SerializedObject.html) serializedObject, string arrayFieldName)
        {
            var arrayType = serializedObject.FindProperty(arrayFieldName).arrayElementType;
            [Debug.Log](Debug.Log.html)($"{arrayFieldName} array type: {arrayType}");
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

