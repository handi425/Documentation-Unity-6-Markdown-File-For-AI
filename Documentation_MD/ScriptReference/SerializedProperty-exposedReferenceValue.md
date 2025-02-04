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

#  [SerializedProperty](SerializedProperty.html).exposedReferenceValue

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

public Object exposedReferenceValue;

### Description

A reference to another Object in the Scene. This reference is resolved in the
context of the SerializedObject containing the SerializedProperty.

Additional resources: [ExposedReference<T0>](ExposedReference_1.html),
[SerializedPropertyType.ExposedReference](SerializedPropertyType.ExposedReference.html),
[SerializedObject.context](SerializedObject-context.html).

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class SerializedPropertyTest : [MonoBehaviour](MonoBehaviour.html)
    {
        public Object mComponent1;
        public Object mComponent2;  
      
        void Start()
        {
            var timeline = [Resources.Load](Resources.Load.html)("myTimeline");
            var so1 = new [SerializedObject](SerializedObject.html)(timeline, mComponent1);
            var so2 = new [SerializedObject](SerializedObject.html)(timeline, mComponent2);  
      
            var theCamera = so1.FindProperty("sceneCamera").exposedReferenceValue;
            var anotherCamera = so2.FindProperty("sceneCamera").exposedReferenceValue;
        }
    }
    

In this example, the same asset is loaded into two different contexts,
`mComponent1` and `mComponent2`. The same object (called “sceneCamera”) in
each context resolves to a different reference to a different Camera Object.

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

