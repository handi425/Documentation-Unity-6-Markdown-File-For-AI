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

# Gyroscope

class in UnityEngine

/

Implemented
in:[UnityEngine.InputLegacyModule](UnityEngine.InputLegacyModule.html)

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

Interface into the Gyroscope.

Use this class to access the gyroscope. The example script below shows how the
Gyroscope class can be used to view the orientation in space of the device.  
  
Underlying sensors used for data population:  
  
**Android** : Gravity, Linear Acceleration, Rotation Vector. [ More
information](https://developer.android.com/guide/topics/sensors/sensors_motion).  
  
**iOS** : Gyroscope, Device-Motion. [ More
information](https://developer.apple.com/documentation/coremotion/cmmotionmanager).

    
    
    // Create a cube with camera vector names on the faces.
    // Allow the device to show named faces as it is oriented.  
      
    using UnityEngine;  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        // Faces for 6 sides of the cube
        private [GameObject](GameObject.html)[] quads = new [GameObject](GameObject.html)[6];  
      
        // Textures for each quad, should be +X, +Y etc
        // with appropriate colors, red, green, blue, etc
        public [Texture](Texture.html)[] labels;  
      
        void Start()
        {
            Input.gyro.enabled = true;
            
            // make camera solid colour and based at the origin
            GetComponent<[Camera](Camera.html)>().backgroundColor = new [Color](Color.html)(49.0f / 255.0f, 77.0f / 255.0f, 121.0f / 255.0f);
            GetComponent<[Camera](Camera.html)>().transform.position = new [Vector3](Vector3.html)(0, 0, 0);
            GetComponent<[Camera](Camera.html)>().clearFlags = [CameraClearFlags.SolidColor](CameraClearFlags.SolidColor.html);  
      
            // create the six quads forming the sides of a cube
            [GameObject](GameObject.html) quad = [GameObject.CreatePrimitive](GameObject.CreatePrimitive.html)([PrimitiveType.Quad](PrimitiveType.Quad.html));  
      
            quads[0] = createQuad(quad, new [Vector3](Vector3.html)(1,   0,   0), new [Vector3](Vector3.html)(0,  90, 0), "plus x",
                new [Color](Color.html)(0.90f, 0.10f, 0.10f, 1), labels[0]);
            quads[1] = createQuad(quad, new [Vector3](Vector3.html)(0,   1,   0), new [Vector3](Vector3.html)(-90,   0, 0), "plus y",
                new [Color](Color.html)(0.10f, 0.90f, 0.10f, 1), labels[1]);
            quads[2] = createQuad(quad, new [Vector3](Vector3.html)(0,   0,   1), new [Vector3](Vector3.html)(0,   0, 0), "plus z",
                new [Color](Color.html)(0.10f, 0.10f, 0.90f, 1), labels[2]);
            quads[3] = createQuad(quad, new [Vector3](Vector3.html)(-1,   0,   0), new [Vector3](Vector3.html)(0, -90, 0), "neg x",
                new [Color](Color.html)(0.90f, 0.50f, 0.50f, 1), labels[3]);
            quads[4] = createQuad(quad, new [Vector3](Vector3.html)(0,  -1,  0), new [Vector3](Vector3.html)(90,   0,  0), "neg y",
                new [Color](Color.html)(0.50f, 0.90f, 0.50f, 1), labels[4]);
            quads[5] = createQuad(quad, new [Vector3](Vector3.html)(0,   0, -1), new [Vector3](Vector3.html)(0, 180,  0), "neg z",
                new [Color](Color.html)(0.50f, 0.50f, 0.90f, 1), labels[5]);  
      
            GameObject.Destroy(quad);
        }  
      
        // make a quad for one side of the cube
        [GameObject](GameObject.html) createQuad([GameObject](GameObject.html) quad, [Vector3](Vector3.html) pos, [Vector3](Vector3.html) rot, string name, [Color](Color.html) col, [Texture](Texture.html) t)
        {
            [Quaternion](Quaternion.html) quat = [Quaternion.Euler](Quaternion.Euler.html)(rot);
            [GameObject](GameObject.html) GO = Instantiate(quad, pos, quat);
            GO.name = name;
            GO.GetComponent<[Renderer](Renderer.html)>().material.color = col;
            GO.GetComponent<[Renderer](Renderer.html)>().material.mainTexture = t;
            GO.transform.localScale += new [Vector3](Vector3.html)(0.25f, 0.25f, 0.25f);
            return GO;
        }  
      
        protected void [Update](PlayerLoop.Update.html)()
        {
            GyroModifyCamera();
        }  
      
        protected void OnGUI()
        {
            GUI.skin.label.fontSize = [Screen.width](Screen-width.html) / 40;  
      
            [GUILayout.Label](GUILayout.Label.html)("[Orientation](Tilemaps.Tilemap.Orientation.html): " + [Screen.orientation](Screen-orientation.html));
            [GUILayout.Label](GUILayout.Label.html)("input.gyro.attitude: " + Input.gyro.attitude);
            [GUILayout.Label](GUILayout.Label.html)("iphone width/font: " + [Screen.width](Screen-width.html) + " : " + GUI.skin.label.fontSize);
        }  
      
        /********************************************/  
      
        // The [Gyroscope](Gyroscope.html) is right-handed.  Unity is left handed.
        // Make the necessary change to the camera.
        void GyroModifyCamera()
        {
            transform.rotation = GyroToUnity(Input.gyro.attitude);
        }  
      
        private static [Quaternion](Quaternion.html) GyroToUnity([Quaternion](Quaternion.html) q)
        {
            return new [Quaternion](Quaternion.html)(q.x, q.y, -q.z, -q.w);
        }
    }
    

![](../StaticFiles/ScriptRefImages/iOSgyroscope.png)  
_iOS Screen-shot showing +Z, +Y and -X._

### Properties

[attitude](Gyroscope-attitude.html)| Returns the attitude (ie, orientation in
space) of the device.  
---|---  
[enabled](Gyroscope-enabled.html)| Sets or retrieves the enabled status of
this gyroscope.  
[gravity](Gyroscope-gravity.html)| Returns the gravity acceleration vector
expressed in the device's reference frame.  
[rotationRate](Gyroscope-rotationRate.html)| Returns rotation rate as measured
by the device's gyroscope.  
[rotationRateUnbiased](Gyroscope-rotationRateUnbiased.html)| Returns unbiased
rotation rate as measured by the device's gyroscope.  
[updateInterval](Gyroscope-updateInterval.html)| Sets or retrieves gyroscope
interval in seconds.  
[userAcceleration](Gyroscope-userAcceleration.html)| Returns the acceleration
that the user is giving to the device.  
  
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

