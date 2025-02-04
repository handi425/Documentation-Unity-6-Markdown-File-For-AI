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

#  [EditorWindow](EditorWindow.html).OnInspectorUpdate()

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

OnInspectorUpdate is called at 10 frames per second to give the inspector a
chance to update.

    
    
    // Simple script that aligns the position of several selected GameObjects
    // with the first selected one.
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;
    using System.Collections;
    using UnityEngine.UIElements;
    
    public class OnInspectorUpdateExample : [EditorWindow](EditorWindow.html)
    {
        bool alignToX = true;
        bool alignToY = true;
        bool alignToZ = true;
        string selected = "";
        string alignTo = "";
    
        [[MenuItem](MenuItem.html)("Examples/OnInspectorUpdate example")]
        static void Init()
        {
            OnInspectorUpdateExample window = (OnInspectorUpdateExample)GetWindow(typeof(OnInspectorUpdateExample));
            window.Show();
        }
    
        void  OnInspectorUpdate()
        {        
            selected = [Selection.activeTransform](Selection-activeTransform.html) ? Selection.activeTransform.name : "";
        }
    
        void CreateGUI()
        {
            var label = new [Label](UIElements.Label.html)("Select various Objects in the [Hierarchy](Unity.Hierarchy.Hierarchy.html) view to align them with the first selected one.");
            rootVisualElement.Add(label);
    
            selected = [Selection.activeTransform](Selection-activeTransform.html) ? Selection.activeTransform.name : "";
    
            var labelSelected = new [Label](UIElements.Label.html)();
            rootVisualElement.Add(labelSelected);
    
            labelSelected.schedule.Execute(() =>
            {
                labelSelected.text = $"Selected object: {selected}";
            }).Every(10);
    
            var toggleX = new [Toggle](UIElements.Toggle.html)();
            toggleX.text = "X";
            toggleX.value = alignToX;
            toggleX.RegisterValueChangedCallback(evt => alignToX = evt.newValue);
            rootVisualElement.Add(toggleX);
    
            var toggleY = new [Toggle](UIElements.Toggle.html)();
            toggleY.text = "Y";
            toggleY.value = alignToY;
            toggleY.RegisterValueChangedCallback(evt => alignToY = evt.newValue);
            rootVisualElement.Add(toggleY);
    
            var toggleZ = new [Toggle](UIElements.Toggle.html)();
            toggleZ.text = "Z";
            toggleZ.value = alignToZ;
            toggleZ.RegisterValueChangedCallback(evt => alignToZ = evt.newValue);
            rootVisualElement.Add(toggleZ);
    
            var buttonAlign = new [Button](UIElements.Button.html)();
            buttonAlign.text = "[Align](UIElements.Align.html)";
            buttonAlign.clicked += () => [Align](UIElements.Align.html)();
            rootVisualElement.Add(buttonAlign);
        }
    
        void [Align](UIElements.Align.html)()
        {
            if (selected == "")
            {
                [Debug.LogError](Debug.LogError.html)("No objects selected to align");
            }
    
            foreach ([Transform](Transform.html) t in [Selection.transforms](Selection-transforms.html))
            {
                [Vector3](Vector3.html) alignementPosition = Selection.activeTransform.position;
                [Vector3](Vector3.html) newPosition;
    
                newPosition.x = alignToX ? alignementPosition.x : t.position.x;
                newPosition.y = alignToY ? alignementPosition.y : t.position.y;
                newPosition.z = alignToZ ? alignementPosition.z : t.position.z;
    
                t.position = newPosition;
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

