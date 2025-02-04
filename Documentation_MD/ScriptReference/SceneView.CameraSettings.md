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

# CameraSettings

class in UnityEditor

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

Use this class to set [SceneView](SceneView.html) Camera properties.

    
    
    // Create a folder (right click in the Assets directory, click **Create** >**Folder**)
    // and name it _Editor_ if one doesn't exist already. Create a new C# script called _CustomSettings_
    // and place it in that folder.  
      
    // This script creates a new menu item **Edit** >**SceneView Settings** >**Update Camera Settings** in the main menu.
    // Use it to update the [Camera](Camera.html) settings in the [Scene](SceneManagement.Scene.html) view.  
      
    using [UnityEditor](UnityEditor.html);  
      
    public class CustomSettings
    {
        [[MenuItem](MenuItem.html)("Edit/[SceneView](SceneView.html) [Settings](CameraEditor.Settings.html)/[Update](PlayerLoop.Update.html) [Camera](Camera.html) [Settings](CameraEditor.Settings.html)")]
        static void UpdateCameraSettings()
        {
            [SceneView.CameraSettings](SceneView.CameraSettings.html) settings = new [SceneView.CameraSettings](SceneView.CameraSettings.html)();
            settings.accelerationEnabled = false;
            settings.speedMin = 1f;
            settings.speedMax = 10f;
            settings.speed = 5f;
            settings.easingEnabled = true;
            settings.easingDuration = 0.6f;
            settings.dynamicClip = false;
            settings.fieldOfView = 120f;
            settings.nearClip = 0.01f;
            settings.farClip = 1000f;
            settings.occlusionCulling = true;
            [SceneView](SceneView.html) sceneView = [SceneView.lastActiveSceneView](SceneView-lastActiveSceneView.html);
            sceneView.cameraSettings = settings;
        }
    }
    

### Properties

[accelerationEnabled](SceneView.CameraSettings-accelerationEnabled.html)|
Enables Camera movement acceleration in the SceneView. This makes the Camera
accelerate for the duration of movement.  
---|---  
[dynamicClip](SceneView.CameraSettings-dynamicClip.html)| When enabled, the
SceneView Camera's near and far clipping planes are calculated relative to the
viewport size of the Scene. When disabled, nearClip and farClip are used
instead.  
[easingDuration](SceneView.CameraSettings-easingDuration.html)| How long it
takes for the speed of the SceneView Camera to accelerate to its initial full
speed. Measured in seconds. Valid values are between [0.1, 2].  
[easingEnabled](SceneView.CameraSettings-easingEnabled.html)| Enables Camera
movement easing in the SceneView. This makes the Camera ease in when it starts
moving, and ease out when it stops.  
[farClip](SceneView.CameraSettings-farClip.html)| The furthest point from the
SceneView Camera that drawing occurs. The valid minimum value is 0.02.  
[fieldOfView](SceneView.CameraSettings-fieldOfView.html)| The height of the
view angle for the SceneView Camera. Measured in degrees vertically, or along
the local Y axis.  
[nearClip](SceneView.CameraSettings-nearClip.html)| The closest point to the
SceneView Camera where drawing occurs. The valid minimum value is 0.01.  
[occlusionCulling](SceneView.CameraSettings-occlusionCulling.html)| Enables
occlusion culling in the SceneView. This prevents Unity from rendering
GameObjects that the Camera cannot see because they are hidden by other
GameObjects.  
[speed](SceneView.CameraSettings-speed.html)| The speed of the SceneView
Camera.  
[speedMax](SceneView.CameraSettings-speedMax.html)| The maximum speed of the
SceneView Camera. Valid values are between [0.0002, 10000].  
[speedMin](SceneView.CameraSettings-speedMin.html)| The minimum speed of the
SceneView Camera. Valid values are between [0.0001, 9999].  
[speedNormalized](SceneView.CameraSettings-speedNormalized.html)| The
normalized speed of the SceneView Camera, relative to the current
minimum/maximum range. Valid values are between [0, 1].  
  
### Constructors

[SceneView.CameraSettings](SceneView.CameraSettings-ctor.html)| Create a new
CameraSettings object.  
---|---  
  
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

