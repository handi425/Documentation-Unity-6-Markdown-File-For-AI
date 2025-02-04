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

#  [InputExtraction](LightTransport.InputExtraction.html).PopulateWorld

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

public static bool
PopulateWorld([LightTransport.InputExtraction.BakeInput](LightTransport.InputExtraction.BakeInput.html)
bakeInput,
[LightTransport.BakeProgressState](LightTransport.BakeProgressState.html)
progress, [LightTransport.IDeviceContext](LightTransport.IDeviceContext.html)
context, [LightTransport.IWorld](LightTransport.IWorld.html) world);

### Parameters

bakeInput | The bake input to use.  
---|---  
progress | Progress tracker.  
context | Device context.  
world | The world to populate with the contents of the bake input.  
  
### Returns

**bool** True if the world was populated successfully.

### Description

Populate the given world from a bake input.

This method generates the world space data structures used by integrators. For
example, acceleration structures, lookup tables, and other data structures
that can be shared between integrators. Related content:
[IWorld](LightTransport.IWorld.html).

    
    
    How to populate a world from a bake input.

// Extract bake input. bool result =
UnityEngine.LightTransport.InputExtraction.ExtractFromScene(out var input);
Assert.IsTrue(result);  
  
// Create context and world. var context = new RadeonRaysContext();
Assert.NotNull(context);  
  
var contextInitialized = context.Initialize(); Assert.AreEqual(true,
contextInitialized); var world = new RadeonRaysWorld();  
  
// Populate the integration world. using var progress = new
BakeProgressState(); var worldResult =
UnityEngine.LightTransport.InputExtraction.PopulateWorld(input, progress,
context, world); Assert.IsTrue(worldResult);  
  
Context.Dispose();

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

