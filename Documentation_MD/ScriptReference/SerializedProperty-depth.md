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

#  [SerializedProperty](SerializedProperty.html).depth

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

public int depth;

### Description

Nesting depth of the property. (Read Only)

Additional resources: [propertyPath](SerializedProperty-propertyPath.html).

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using System.Text;
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class SerializePropertyDepthExample : [ScriptableObject](ScriptableObject.html)
    {
        // Declare fields to demonstrate data at different depths
        public int m_depth0;  
      
        [Serializable]
        public struct Nested
        {
            public int m_depth1;  
      
            [Serializable]
            public struct NestedInNested
            {
                public int m_depth2;
                public [Vector2](Vector2.html) m_vectorDepth2; // Contains x,y at depth 3
            };
            public NestedInNested m_Nested1;
        };
        public Nested m_Nested0;
        public bool m_boolDepth0;  
      
        [[MenuItem](MenuItem.html)("Example/[SerializedProperty](SerializedProperty.html) depth Example")]
        static void DepthExample()
        {
            var scriptableObject = [ScriptableObject.CreateInstance](ScriptableObject.CreateInstance.html)<SerializePropertyDepthExample>();  
      
            using (var serializedObject = new [SerializedObject](SerializedObject.html)(scriptableObject))
            {
                var report = new StringBuilder();  
      
                var iterator = serializedObject.FindProperty("m_depth0");  
      
                const bool visitChildren = true;
                do
                {
                    report.AppendLine($"Found {iterator.propertyPath} (depth {iterator.depth})");
                }
                while (iterator.Next(visitChildren));  
      
                //Output:
                //Found m_depth0 (depth 0)
                //Found m_Nested0 (depth 0)
                //Found m_Nested0.m_depth1 (depth 1)
                //Found m_Nested0.m_Nested1 (depth 1)
                //Found m_Nested0.m_Nested1.m_depth2 (depth 2)
                //Found m_Nested0.m_Nested1.m_vectorDepth2 (depth 2)
                //Found m_Nested0.m_Nested1.m_vectorDepth2.x (depth 3)
                //Found m_Nested0.m_Nested1.m_vectorDepth2.y (depth 3)
                //Found m_boolDepth0 (depth 0)
                [Debug.Log](Debug.Log.html)(report.ToString());
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

