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

#
[ProfilerModuleViewController](Unity.Profiling.Editor.ProfilerModuleViewController.html).CreateView

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

protected [UIElements.VisualElement](UIElements.VisualElement.html)
CreateView();

### Returns

**VisualElement** Returns the view controller’s view. A
[VisualElement](UIElements.VisualElement.html).

### Description

Creates the view controller’s view. Unity calls this method automatically when
it is about to display the view controller’s view for the first time.

You must override this method to construct the view controller’s view
hierarchy. To do this, load a visual tree from a [UXML file](../Manual/UIE-
WritingUXMLTemplate.html), or construct a view directly in C#, as shown in the
example code.

    
    
    using Unity.Profiling.Editor;
    using [UnityEditor](UnityEditor.html);
    using UnityEngine.UIElements;  
      
    public class SingleCounterViewController : [ProfilerModuleViewController](Unity.Profiling.Editor.ProfilerModuleViewController.html)
    {
        [ProfilerCounterDescriptor](Unity.Profiling.Editor.ProfilerCounterDescriptor.html) m_Counter;
        [Label](UIElements.Label.html) m_CounterLabel;  
      
        public SingleCounterViewController([ProfilerWindow](ProfilerWindow.html) profilerWindow, [ProfilerCounterDescriptor](Unity.Profiling.Editor.ProfilerCounterDescriptor.html) counter) : base(profilerWindow)
        {
            m_Counter = counter;
        }  
      
        protected override [VisualElement](UIElements.VisualElement.html) CreateView()
        {
            // Create a simple view with a single label.
            var view = new [VisualElement](UIElements.VisualElement.html)();
            m_CounterLabel = new [Label](UIElements.Label.html)();
            view.Add(m_CounterLabel);  
      
            // Subscribe to [Profiler](Profiling.Profiler.html) window SelectedFrameIndexChanged event.
            [ProfilerWindow.SelectedFrameIndexChanged](ProfilerWindow.SelectedFrameIndexChanged.html) += OnSelectedFrameIndexChanged;  
      
            // Populate label with counter value in selected frame.
            ReloadData();  
      
            return view;
        }  
      
        protected override void Dispose(bool disposing)
        {
            if (!disposing)
                return;  
      
            // Unsubscribe from [Profiler](Profiling.Profiler.html) window SelectedFrameIndexChanged event.
            [ProfilerWindow.SelectedFrameIndexChanged](ProfilerWindow.SelectedFrameIndexChanged.html) -= OnSelectedFrameIndexChanged;  
      
            base.Dispose(disposing);
        }  
      
        void OnSelectedFrameIndexChanged(long selectedFrame)
        {
            // [Update](PlayerLoop.Update.html) label with counter value in selected frame.
            ReloadData();
        }  
      
        void ReloadData()
        {
            // [Update](PlayerLoop.Update.html) label text with formatted counter value in selected frame.
            var selectedFrameIndexInt32 = System.Convert.ToInt32([ProfilerWindow.selectedFrameIndex](ProfilerWindow-selectedFrameIndex.html));
            var formattedCounterValue = UnityEditorInternal.ProfilerDriver.GetFormattedCounterValue(selectedFrameIndexInt32, m_Counter.CategoryName, m_Counter.Name);
            m_CounterLabel.text = $"{m_Counter}: {formattedCounterValue}";
        }
    }
    

Additional resources:
[ProfilerWindow.SelectedFrameIndexChanged](ProfilerWindow.SelectedFrameIndexChanged.html),
[ProfilerModule](Unity.Profiling.Editor.ProfilerModule.html),
[ProfilerCounterDescriptor](Unity.Profiling.Editor.ProfilerCounterDescriptor.html).

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

