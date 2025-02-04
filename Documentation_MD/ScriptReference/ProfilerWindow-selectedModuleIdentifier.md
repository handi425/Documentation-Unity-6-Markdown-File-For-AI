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

#  [ProfilerWindow](ProfilerWindow.html).selectedModuleIdentifier

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

public string selectedModuleIdentifier;

### Description

The identifier of the [Profiler module](../Manual/ProfilerWindow#modules.html)
that is currently selected in the Profiler Window, or null if no Module is
currently selected.

The [Profiler Window](../Manual/ProfilerWindow.html) shows the Module Details
panel in its bottom half for the currently selected module. Compare this
field's value to constants like
[ProfilerWindow.cpuModuleIdentifier](ProfilerWindow-cpuModuleIdentifier.html)
and [ProfilerWindow.gpuModuleIdentifier](ProfilerWindow-
gpuModuleIdentifier.html) to check which module is currently selected.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.Profiling;
    using UnityEngine;  
      
    public class Example : [EditorWindow](EditorWindow.html)
    {
        [ProfilerWindow](ProfilerWindow.html) m_Profiler = null;
        [[MenuItem](MenuItem.html)("Window/Analysis/[Profiler](Profiling.Profiler.html) Extension")]
        public static void ShowExampleWindow()
        {
            var window = GetWindow<Example>();
            window.m_Profiler = [EditorWindow.GetWindow](EditorWindow.GetWindow.html)<[ProfilerWindow](ProfilerWindow.html)>();
        }  
      
        void OnGUI()
        {
            // First make sure there is an open [Profiler](Profiling.Profiler.html) Window
            if (m_Profiler == null)
                m_Profiler = [EditorWindow.GetWindow](EditorWindow.GetWindow.html)<[ProfilerWindow](ProfilerWindow.html)>();
            // If the currently selected Module is not the CPU Usage module, setting the selection will not be visible to the user immediately
            if (m_Profiler.selectedModuleIdentifier == [ProfilerWindow.cpuModuleIdentifier](ProfilerWindow-cpuModuleIdentifier.html))
            {
                // Get the CPU Usage [Profiler](Profiling.Profiler.html) module's selection controller interface to interact with the selection
                var cpuSampleSelectionController = m_Profiler.GetFrameTimeViewSampleSelectionController([ProfilerWindow.cpuModuleIdentifier](ProfilerWindow-cpuModuleIdentifier.html));
                // If the current selection object is null, there is no selection to print out.
                using (new [EditorGUI.DisabledScope](EditorGUI.DisabledScope.html)(cpuSampleSelectionController.selection == null))
                {
                    if ([GUILayout.Button](GUILayout.Button.html)("Print current [Selection](Selection.html)"))
                    {
                        // Get the currently shown selection and log out some of its details
                        var selection = cpuSampleSelectionController.selection;
                        [Debug.Log](Debug.Log.html)($"The sample currently selected in the CPU Usage [Profiler](Profiling.Profiler.html) module is {selection.sampleDisplayName} at a depth of {selection.markerPathDepth}.");
                    }
                }
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

