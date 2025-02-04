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
[ProfilerModule](Unity.Profiling.Editor.ProfilerModule.html).CreateDetailsViewController

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

public
[Unity.Profiling.Editor.ProfilerModuleViewController](Unity.Profiling.Editor.ProfilerModuleViewController.html)
CreateDetailsViewController();

### Returns

**ProfilerModuleViewController** Returns a
[ProfilerModuleViewController](Unity.Profiling.Editor.ProfilerModuleViewController.html)
derived object that draws the module’s Details View in the Profiler window.
The default value is a view controller that displays a list of the module’s
chart counters alongside their current values in the selected frame.

### Description

Creates a View Controller object that draws the Profiler module’s Details View
in the Profiler window. Unity calls this method automatically when the module
is selected in the Profiler window.

To present a bespoke visualization of your performance data when your module
is selected, override this method. To do this, define a new
[ProfilerModuleViewController](Unity.Profiling.Editor.ProfilerModuleViewController.html)
derived type, where the custom drawing can be implemented, and return a new
instance of it in this method.  
  
![](../StaticFiles/ScriptRefImages/ProfilerModuleCustomDetailsView.png).

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using Unity.Profiling;
    using Unity.Profiling.Editor;
    using [UnityEditor](UnityEditor.html);
    using UnityEngine.UIElements;  
      
    //--Module--  
      
    [Serializable]
    [ProfilerModuleMetadata("Garbage Collection")]
    public class GarbageCollectionProfilerModule : [ProfilerModule](Unity.Profiling.Editor.ProfilerModule.html)
    {
        static readonly [ProfilerCounterDescriptor](Unity.Profiling.Editor.ProfilerCounterDescriptor.html)[] k_ChartCounters = new [ProfilerCounterDescriptor](Unity.Profiling.Editor.ProfilerCounterDescriptor.html)[]
        {
            new [ProfilerCounterDescriptor](Unity.Profiling.Editor.ProfilerCounterDescriptor.html)("GC Reserved Memory", [ProfilerCategory.Memory](Unity.Profiling.ProfilerCategory.Memory.html)),
            new [ProfilerCounterDescriptor](Unity.Profiling.Editor.ProfilerCounterDescriptor.html)("GC Used Memory", [ProfilerCategory.Memory](Unity.Profiling.ProfilerCategory.Memory.html)),
            new [ProfilerCounterDescriptor](Unity.Profiling.Editor.ProfilerCounterDescriptor.html)("GC Allocated In Frame", [ProfilerCategory.Memory](Unity.Profiling.ProfilerCategory.Memory.html)),
        };  
      
        // Specify a list of [Profiler](Profiling.Profiler.html) category names, which should be auto-enabled when the module is active.
        static readonly string[] k_AutoEnabledCategoryNames = new string[]
        {
            ProfilerCategory.Memory.Name,
        };  
      
        public GarbageCollectionProfilerModule() : base(k_ChartCounters, autoEnabledCategoryNames: k_AutoEnabledCategoryNames) { }  
      
        public override [ProfilerModuleViewController](Unity.Profiling.Editor.ProfilerModuleViewController.html) CreateDetailsViewController()
        {
            return new GarbageCollectionDetailsViewController([ProfilerWindow](ProfilerWindow.html));
        }
    }  
      
    //--Module Custom Drawing--  
      
    public class GarbageCollectionDetailsViewController : [ProfilerModuleViewController](Unity.Profiling.Editor.ProfilerModuleViewController.html)
    {
        const string k_UxmlResourceName = "Assets/[Editor](Editor.html)/GarbageCollectionDetailsView.uxml";
        const string k_UxmlElementId_GarbageCollectionDetailsView**BarFill = "garbage-collection-details-view** bar-fill";
        const string k_UxmlElementId_GarbageCollectionDetailsView**BarLabel = "garbage-collection-details-view** bar-label";  
      
        static readonly [ProfilerCounterDescriptor](Unity.Profiling.Editor.ProfilerCounterDescriptor.html) k_GcReservedMemoryCounterDescriptor = new [ProfilerCounterDescriptor](Unity.Profiling.Editor.ProfilerCounterDescriptor.html)("GC Reserved Memory", [ProfilerCategory.Memory](Unity.Profiling.ProfilerCategory.Memory.html));
        static readonly [ProfilerCounterDescriptor](Unity.Profiling.Editor.ProfilerCounterDescriptor.html) k_GcUsedMemoryCounterDescriptor = new [ProfilerCounterDescriptor](Unity.Profiling.Editor.ProfilerCounterDescriptor.html)("GC Used Memory", [ProfilerCategory.Memory](Unity.Profiling.ProfilerCategory.Memory.html));  
      
        [VisualElement](UIElements.VisualElement.html) m_BarFill;
        [Label](UIElements.Label.html) m_BarLabel;  
      
        public GarbageCollectionDetailsViewController([ProfilerWindow](ProfilerWindow.html) profilerWindow) : base(profilerWindow) { }  
      
        protected override [VisualElement](UIElements.VisualElement.html) CreateView()
        {
            var template = [AssetDatabase.LoadAssetAtPath](AssetDatabase.LoadAssetAtPath.html)<[VisualTreeAsset](UIElements.VisualTreeAsset.html)>(k_UxmlResourceName);
            var view = template.Instantiate();  
      
            m_BarFill = view.Q<[VisualElement](UIElements.VisualElement.html)>(name: k_UxmlElementId_GarbageCollectionDetailsView__BarFill);
            m_BarLabel = view.Q<[Label](UIElements.Label.html)>(name: k_UxmlElementId_GarbageCollectionDetailsView__BarLabel);  
      
            ReloadData([ProfilerWindow.selectedFrameIndex](ProfilerWindow-selectedFrameIndex.html));
            [ProfilerWindow.SelectedFrameIndexChanged](ProfilerWindow.SelectedFrameIndexChanged.html) += OnSelectedFrameIndexChanged;  
      
            return view;
        }  
      
        protected override void Dispose(bool disposing)
        {
            if (!disposing)
                return;  
      
            [ProfilerWindow.SelectedFrameIndexChanged](ProfilerWindow.SelectedFrameIndexChanged.html) -= OnSelectedFrameIndexChanged;
            base.Dispose(disposing);
        }  
      
        void OnSelectedFrameIndexChanged(long selectedFrameIndex)
        {
            ReloadData(selectedFrameIndex);
        }  
      
        void ReloadData(long selectedFrameIndex)
        {
            long gcReservedBytes = 0;
            long gcUsedBytes = 0;  
      
            var selectedFrameIndexInt32 = Convert.ToInt32(selectedFrameIndex);
            using (var frameData = UnityEditorInternal.ProfilerDriver.GetRawFrameDataView(selectedFrameIndexInt32, 0))
            {
                if (frameData == null || !frameData.valid)
                    return;  
      
                var gcReservedBytesMarkerId = frameData.GetMarkerId(k_GcReservedMemoryCounterDescriptor.Name);
                gcReservedBytes = frameData.GetCounterValueAsLong(gcReservedBytesMarkerId);  
      
                var gcUsedBytesMarkerId = frameData.GetMarkerId(k_GcUsedMemoryCounterDescriptor.Name);
                gcUsedBytes = frameData.GetCounterValueAsLong(gcUsedBytesMarkerId);
            }  
      
            float gcUsedBytesScalar = (float)gcUsedBytes / gcReservedBytes;
            m_BarFill.style.width = new [Length](UIElements.Length.html)(gcUsedBytesScalar * 100, [LengthUnit.Percent](UIElements.LengthUnit.Percent.html));
            m_BarLabel.text = $"{[EditorUtility.FormatBytes](EditorUtility.FormatBytes.html)(gcUsedBytes)} / {[EditorUtility.FormatBytes](EditorUtility.FormatBytes.html)(gcReservedBytes)}";
        }
    }  
      
    //--Assets/[Editor](Editor.html)/GarbageCollectionDetailsView.uxml--  
      
    <?xml version="1.0" encoding="utf-8"?>
    <engine:UXML
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xmlns:engine="UnityEngine.UIElements"
        xmlns:editor="UnityEditor.UIElements"
        xsi:noNamespaceSchemaLocation="../../UIElementsSchema/UIElements.xsd">
      <engine:Style src="GarbageCollectionDetailsView.uss"/>
      <engine:[VisualElement](UIElements.VisualElement.html) name="garbage-collection-details-view">
        <engine:[Label](UIElements.Label.html) name="garbage-collection-details-view**title-label" text="Garbage Collection"/ >
        <engine:VisualElement name="garbage-collection-details-view**bar">
          <engine:[VisualElement](UIElements.VisualElement.html) name="garbage-collection-details-view**bar-fill"/ >
        </engine:VisualElement>
        <engine:Label name="garbage-collection-details-view**bar-label"/>
      </engine:[VisualElement](UIElements.VisualElement.html)>
    </engine:UXML>  
      
    //--Assets/[Editor](Editor.html)/GarbageCollectionDetailsView.uss--  
      
    #garbage-collection-details-view
    {
        flex-grow: 1;
        margin: 8px;
    }  
      
    #garbage-collection-details-view__title-label
    {
        -unity-font-style: bold;
        margin-bottom: 8px;
    }  
      
    #garbage-collection-details-view__bar
    {
        background-color: gray;
        flex-direction: row;
        height: 20px;
    }  
      
    #garbage-collection-details-view__bar-fill
    {
        background-color: #B2194C;
        position: absolute;
        height: 100%;
    }
    

Additional resources:
[ProfilerModuleViewController](Unity.Profiling.Editor.ProfilerModuleViewController.html).

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

