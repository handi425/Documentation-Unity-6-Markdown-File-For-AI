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

#  [ProfilerWindow](ProfilerWindow.html).SelectedFrameIndexChanged

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

### Parameters

value | The zero-based index of the frame currently selected in the Profiler Window. A long.  
---|---  
  
### Description

Calls the methods in its invocation list when the Profiler window’s selected
frame index changes.

The Profiler window’s selected frame index may change for a variety of
reasons, such as a new frame being captured, the user selecting a new frame,
or a new capture being loaded.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    public class Example : [EditorWindow](EditorWindow.html)
    {
        [ProfilerWindow](ProfilerWindow.html) m_Profiler;
        long m_SelectedFrameIndex;  
      
        [[MenuItem](MenuItem.html)("Window/Analysis/[Profiler](Profiling.Profiler.html) Extension")]
        public static void ShowExampleWindow()
        {
            GetWindow<Example>();
        }  
      
        void OnEnable()
        {
            // Make sure there is an open [Profiler](Profiling.Profiler.html) Window.
            if (m_Profiler == null)
                m_Profiler = [EditorWindow.GetWindow](EditorWindow.GetWindow.html)<[ProfilerWindow](ProfilerWindow.html)>();  
      
            // Subscribe to the [Profiler](Profiling.Profiler.html) window's SelectedFrameIndexChanged event.
            m_Profiler.SelectedFrameIndexChanged += OnProfilerSelectedFrameIndexChanged;
        }  
      
        private void OnGUI()
        {
            [GUILayout.Label](GUILayout.Label.html)($"The selected frame in the [Profiler](Profiling.Profiler.html) window is {m_SelectedFrameIndex}.");
        }  
      
        private void OnDisable()
        {
            // Unsubscribe from the [Profiler](Profiling.Profiler.html) window's SelectedFrameIndexChanged event.
            m_Profiler.SelectedFrameIndexChanged -= OnProfilerSelectedFrameIndexChanged;
        }  
      
        void OnProfilerSelectedFrameIndexChanged(long selectedFrameIndex)
        {
            // [Update](PlayerLoop.Update.html) the [GUI](GUI.html) with the selected [Profiler](Profiling.Profiler.html) frame.
            m_SelectedFrameIndex = selectedFrameIndex;
            Repaint();
        }
    }
    

Additional resources: [ProfilerWindow.selectedFrameIndex](ProfilerWindow-
selectedFrameIndex.html).

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

