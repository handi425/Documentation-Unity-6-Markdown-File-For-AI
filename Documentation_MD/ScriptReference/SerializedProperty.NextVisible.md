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

#  [SerializedProperty](SerializedProperty.html).NextVisible

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

public bool NextVisible(bool enterChildren);

### Description

Move to next visible property.

Additional resources: [Next](SerializedProperty.Next.html),
[hasVisibleChildren](SerializedProperty-hasVisibleChildren.html),
[isExpanded](SerializedProperty-isExpanded.html),
[Reset](SerializedProperty.Reset.html),
[HideInInspector](HideInInspector.html).

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using System.Text;
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class SerializePropertyNextVisible : [ScriptableObject](ScriptableObject.html)
    {
        public bool m_SeeMe1;  
      
        [[HideInInspector](HideInInspector.html)]
        public bool m_HideMe1;  
      
        [[SerializeField](SerializeField.html)]
        private bool m_SeeMe2;  
      
        [[HideInInspector](HideInInspector.html)]
        public bool m_HideMe2;  
      
        [[MenuItem](MenuItem.html)("Example/[SerializedProperty](SerializedProperty.html) NextVisible Example")]
        static void TestNextOnCyclicGraph()
        {
            var scriptableObject = [ScriptableObject.CreateInstance](ScriptableObject.CreateInstance.html)<SerializePropertyNextVisible>();
            using (var serializedObject = new [SerializedObject](SerializedObject.html)(scriptableObject))
            {
                var serializedProperty = serializedObject.GetIterator();  
      
                var sb = new StringBuilder();
                sb.AppendLine("Visible Properties:");  
      
                // Move from the root to the first visible property
                bool visitChild = true;
                serializedProperty.NextVisible(visitChild);  
      
                // Rest of scan stays at same level
                visitChild = false;
                do
                {
                    // Note: some properties from the supporting Unity base objects are exposed
                    // (and visible in the inspector), for example "m_Script".
                    sb.AppendLine(serializedProperty.name);
                }
                while (serializedProperty.NextVisible(visitChild));  
      
                /*Expected output
                m_Script
                m_SeeMe1
                m_SeeMe2
                */
                [Debug.Log](Debug.Log.html)(sb.ToString());
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

