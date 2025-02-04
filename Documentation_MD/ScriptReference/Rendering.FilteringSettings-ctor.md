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

# FilteringSettings Constructor

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

public FilteringSettings(Nullable<RenderQueueRange> renderQueueRange =
RenderQueueRange.all, int layerMask, uint renderingLayerMask, int
excludeMotionVectorObjects);

### Parameters

renderQueueRange | A [RenderQueueRange](Rendering.RenderQueueRange.html) struct that sets the value of [renderQueueRange](Rendering.FilteringSettings-renderQueueRange.html). Unity renders objects whose [Material.renderQueue](Material-renderQueue.html) value is within the given range. The default value is `RenderQueueRange.all`.  
---|---  
layerMask | A bit mask that sets the value of [layerMask](Rendering.FilteringSettings-layerMask.html). Unity renders objects whose [GameObject.layer](GameObject-layer.html) value is enabled in this bit mask. The default value is `-1`.  
renderingLayerMask | A bit mask that sets the value of [renderingLayerMask](Rendering.FilteringSettings-renderingLayerMask.html). Unity renders objects whose [Renderer.renderingLayerMask](Renderer-renderingLayerMask.html) value is enabled in this bit mask. The default value is `uint.MaxValue`.  
excludeMotionVectorObjects | An int that sets the value of [excludeMotionVectorObjects](Rendering.FilteringSettings-excludeMotionVectorObjects.html). When this is `1`, Unity excludes objects that have a motion pass enabled, or have changed position since the last frame. The default value is `0`.  
  
### Description

Creates a `FilteringSettings` struct for use with
Rendering.ScriptableRenderContext.DrawRenderers.

**Note:** If you call `new FilteringSettings()` without any parameters, Unity
creates an empty `FilteringSettings` struct. An empty struct contains no data
and all internal values default to 0; for example, it has a `layerMask` value
of 0, and so on. Unless you overwrite its properties, this empty struct tells
Unity to exclude all objects.  
  
If you call this constructor with one or more parameters, Unity sets any
unspecified values to the default. The default value for each property
performs no filtering. To create a `FilteringSettings` struct with all default
values, use [FilteringSettings.defaultValue](Rendering.FilteringSettings-
defaultValue.html).  
  
This example demonstrates the syntax for creating a `FilteringSettings` struct
with some non-default values.

    
    
    using UnityEngine;
    using UnityEngine.Rendering;  
      
    public class FilteringSettingsExample
    {
        public [FilteringSettings](Rendering.FilteringSettings.html) CreateFilteringSettings()
        {
            // Instantiate a [RenderQueueRange](Rendering.RenderQueueRange.html) struct that represents the [RenderQueue](Rendering.RenderQueue.html) values you want to render
            // In this example, render materials whose [RenderQueue](Rendering.RenderQueue.html) value is in the opaque range
            var desiredRenderQueueRange = [RenderQueueRange.opaque](Rendering.RenderQueueRange-opaque.html);  
      
            // Create a bit mask that represents the layers you want to render
            // In this example, only render objects on layer 0 (the "Default" layer)
            int layerIndex = 0;
            int layerMask = 1 << layerIndex;  
      
            // Instantiate a [FilteringSettings](Rendering.FilteringSettings.html) struct with the desired values
            // Unity sets any unspecified values to the same as FilteringSettings.default
            [FilteringSettings](Rendering.FilteringSettings.html) filteringSettings = new [FilteringSettings](Rendering.FilteringSettings.html)(desiredRenderQueueRange, layerMask);  
      
            return filteringSettings;
        }
    }
    

Additional resources: ScriptableRenderContext.DrawRenderers, [Creating a
simple render loop in a custom render pipeline](../Manual/srp-creating-simple-
render-loop.html).

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

