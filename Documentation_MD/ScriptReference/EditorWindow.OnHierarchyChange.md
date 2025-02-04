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

#  [EditorWindow](EditorWindow.html).OnHierarchyChange()

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

### Description

Handler for message that is sent when an object or group of objects in the
hierarchy changes.

Actions that trigger this message include creating, renaming, reparenting, or
destroying objects in the current hierarchy, as well as loading, unloading,
renaming, or reordering loaded Scenes. Note that the message is not sent
immediately in response to these actions, but rather during the next update of
the editor application.  
  
Actions taken with objects that have
[HideFlags.HideInHierarchy](HideFlags.HideInHierarchy.html) set will not cause
this message to be sent, but changing [Object.hideFlags](Object-
hideFlags.html) will.  
  
The [OnHierarchyChange](EditorWindow.OnHierarchyChange.html)() is added to the
Unity editor. Adding a new GameObject into the Scene, or changing the position
of a GameObject in the Inspector will be observed by
[OnHierarchyChange](EditorWindow.OnHierarchyChange.html)(). Similarly, changes
to the rotation and scale will be seen.  
  
![](../StaticFiles/ScriptRefImages/EditorWindowOnHierarchyChange.gif)  
_An animation showing how the OnHierarchyChange can be used._  
  
Additional resources: EditorApplication.hierarchyChange  
  
The following example script created an [EditorWindow](EditorWindow.html) that
monitors the number of objects and updates whenever the hierarchy changes.
Copy it into a file called HierarchyMonitorWindow.cs and put it in a folder
called Editor.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;
    using UnityEngine.UIElements;
    
    class HierarchyMonitorWindow : [EditorWindow](EditorWindow.html)
    {
        [[MenuItem](MenuItem.html)("Examples/[Hierarchy](Unity.Hierarchy.Hierarchy.html) Monitor")]
        static void CreateWindow()
        {
            [EditorWindow.GetWindow](EditorWindow.GetWindow.html)<HierarchyMonitorWindow>();
        }
    
        [[SerializeField](SerializeField.html)]
        int m_NumberVisible;
    
        void OnEnable()
        {
            titleContent.text = "[Hierarchy](Unity.Hierarchy.Hierarchy.html) Monitor";
            // Manually call the event handler when the window is first loaded so its contents are up-to-date.
            OnHierarchyChange();
        }
    
        void OnHierarchyChange()
        {
            var all = [Resources.FindObjectsOfTypeAll](Resources.FindObjectsOfTypeAll.html)(typeof([GameObject](GameObject.html)));
            m_NumberVisible = CountVisibleObjects(all);
            var label = rootVisualElement.Q<[Label](UIElements.Label.html)>();
            if (label != null)
                label.text = $"There are currently {m_NumberVisible} GameObjects visible in the hierarchy.";
        }
    
        int CountVisibleObjects(Object[] objects)
        {
            int count = 0;
            foreach (var obj in objects)
            {
                var gameObject = obj as [GameObject](GameObject.html);
                if (gameObject != null && (gameObject.hideFlags & [HideFlags.HideInHierarchy](HideFlags.HideInHierarchy.html)) != [HideFlags.HideInHierarchy](HideFlags.HideInHierarchy.html))
                {
                    count++;
                }
            }
            return count;
        }
    
        void CreateGUI()
        {
            var label = new [Label](UIElements.Label.html)($"There are currently {m_NumberVisible} GameObjects visible in the hierarchy.");
            rootVisualElement.Add(label);
        }
    }
    

Another simple example.

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);
    using UnityEngine.UIElements;
    
    public class OnHierarchyChangeExample : [EditorWindow](EditorWindow.html)
    {
        static int count = 0;
    
        [[MenuItem](MenuItem.html)("Examples/OnHierarchyChange Example")]
        static void Init()
        {
            OnHierarchyChangeExample window = (OnHierarchyChangeExample)GetWindow(typeof(OnHierarchyChangeExample));
            window.Show();
        }
    
        void OnHierarchyChange()
        {
            count += 1;
        }
    
        void CreateGUI()
        {
            var label = new [Label](UIElements.Label.html)();
            rootVisualElement.Add(label);
    
            label.schedule.Execute(() =>
            {
                label.text = $"OnHierarchyChange: {count}";
            }).Every(10);
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

