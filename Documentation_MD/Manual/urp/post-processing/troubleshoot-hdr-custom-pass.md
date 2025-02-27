[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/post-processing/troubleshoot-hdr-custom-pass.html)
  * [中文](/cn/current/Manual/urp/post-processing/troubleshoot-hdr-custom-pass.html)
  * [日本語](/ja/current/Manual/urp/post-processing/troubleshoot-hdr-custom-pass.html)
  * [한국어](/kr/current/Manual/urp/post-processing/troubleshoot-hdr-custom-pass.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/post-processing/troubleshoot-hdr-custom-pass.html)
  * [中文](/cn/current/Manual/urp/post-processing/troubleshoot-hdr-custom-pass.html)
  * [日本語](/ja/current/Manual/urp/post-processing/troubleshoot-hdr-custom-pass.html)
  * [한국어](/kr/current/Manual/urp/post-processing/troubleshoot-hdr-custom-pass.html)

  * [Rendering](../../rendering-and-post-processing.html)
  * [Color](../../graphics-color.html)
  * [High dynamic range (HDR)](../../hdr-landing.html)
  * [HDR](../../urp/post-processing/hdr-in-urp.html)
  * Troubleshooting Scriptable Render Passes with HDR Output in URP

[](../../urp/post-processing/hdr-output-implement-custom-overlay.html)

Implement an HDR Output compatible custom overlay in URP

[](../../graphics-performance-profiling.html)

Graphics performance and profiling

# Troubleshooting Scriptable Render Passes with HDR Output in URP

High Dynamic Range (HDR) Output changes the inputs to your scriptable render
pass when it applies tone mapping and color space conversions. These changes
can cause your scriptable render pass to produce incorrect results. This means
that when you use **HDR** high dynamic range  
See in [Glossary](../../Glossary.html#HDR) Output and a scriptable render pass
that happens in or after the AfterRenderingPostProcessing injection point, you
need to account for the changes HDR Output makes. This also applies when you
want to add overlays during or after **post-processing** A process that
improves product visuals by applying filters and effects before the image
appears on screen. You can use post-processing effects to simulate physical
camera and film properties, for example Bloom and Depth of Field. [More
info](../../PostProcessingOverview.html) post processing, postprocessing,
postprocess  
See in [Glossary](../../Glossary.html#post-processing), such as **UI**(User
Interface) Allows a user to interact with your application. Unity currently
supports three UI systems. [More info](../../UI-system-compare.html)  
See in [Glossary](../../Glossary.html#UI) or output from other **cameras** A
component which creates an image of a particular viewpoint in your scene. The
output is either drawn to the screen or captured as a texture. [More
info](../../CamerasOverview.html)  
See in [Glossary](../../Glossary.html#Camera), because you need to work with
the color gamut that results from HDR Output. To make a scriptable render pass
work with the changes HDR Output makes, you must manually perform tone mapping
and convert color space in a script.

However, if you add your scriptable render pass at or before the
BeforeRenderingPostProcessing injection point, you don’t need to make any
changes for compatibility with HDR Output. This is because Unity executes your
scriptable render pass before it renders the HDR Output.

**Note** : You can avoid this problem when you use a camera stack to render
camera output before Unity performs tone mapping. Unity then applies HDR
Output processing to the last camera in the stack. To learn how to set up a
camera stack, refer to [Camera stacking](../camera-stacking.html).

##  Tone map and convert color space in a script

To make a scriptable render pass pass work with the changes HDR Output makes
to color space and dynamic range, use the `SetupHDROutput` function to apply
tone mapping and color space conversion to the material the scriptable render
pass alters:

  1. Open the C# script which contains the Scriptable Render Pass you wish to use with HDR Output.

  2. Add a method with the name `SetupHDROutput` to the Render Pass class.

The following script gives an example of how to use the `SetupHDROutput`
function:

    
        class CustomFullScreenRenderPass : ScriptableRenderPass
    {
        // Leave your existing Render Pass code here
    
        static void SetupHDROutput(ref CameraData cameraData, Material material)
        {
            // This is where most HDR related code is added
        }
    }
    

  3. Add an `if` statement to check whether HDR Output is active and if the camera has post-processing enabled. If either condition is not met, disable the HDR Output **shader** A program that runs on the GPU. [More info](../../Shaders.html)  
See in [Glossary](../../Glossary.html#Shader) keywords to reduce resource
usage.

    
        static void SetupHDROutput(ref CameraData cameraData, Material material)
    {
        // If post processing is enabled, color grading has already applied tone mapping
        // As a result the input here will be in the display colorspace (Rec2020, P3, etc) and in nits
        if (cameraData.isHDROutputActive && cameraData.postProcessEnabled)
        {
    
        }
        else
        {
            // If HDR output is disabled, disable HDR output-related keywords
            // If post processing is disabled, the final pass will do the color conversion so there is
            // no need to account for HDR Output
            material.DisableKeyword(HDROutputUtils.ShaderKeywords.HDR_INPUT);
        }
    }
    

  4. Create variables to retrieve and store the luminance information from the display as shown below.
    
        if (cameraData.isHDROutputActive && cameraData.postProcessEnabled)
    {
        // Get luminance information from the display, these define the dynamic range of the display.
        float minNits = cameraData.hdrDisplayInformation.minToneMapLuminance;
        float maxNits = cameraData.hdrDisplayInformation.maxToneMapLuminance;
        float paperWhite = cameraData.hdrDisplayInformation.paperWhiteNits;
    }
    else
    {
        // If HDR output is disabled, disable HDR output-related keywords
        // If post processing is disabled, the final pass will do the color conversion so there is
        // no need to account for HDR Output
        material.DisableKeyword(HDROutputUtils.ShaderKeywords.HDR_INPUT);
    }
    

  5. Retrieve the **tonemapping** The process of remapping HDR values of an image into a range suitable to be displayed on screen. [More info](../../PostProcessingOverview.html)  
See in [Glossary](../../Glossary.html#Tonemapping) component from the Volume
Manager.

    
        if (cameraData.isHDROutputActive && cameraData.postProcessEnabled)
    {
        var tonemapping = VolumeManager.instance.stack.GetComponent<Tonemapping>();
    
        // Get luminance information from the display, these define the dynamic range of the display.
        float minNits = cameraData.hdrDisplayInformation.minToneMapLuminance;
        float maxNits = cameraData.hdrDisplayInformation.maxToneMapLuminance;
        float paperWhite = cameraData.hdrDisplayInformation.paperWhiteNits;
    }
    

  6. Add another `if` statement to check whether a tonemapping component is present. If a tonemapping component is found, this can override the luminance data from the display.
    
        if (cameraData.isHDROutputActive && cameraData.postProcessEnabled)
    {
        var tonemapping = VolumeManager.instance.stack.GetComponent<Tonemapping>();
    
        // Get luminance information from the display, these define the dynamic range of the display.
        float minNits = cameraData.hdrDisplayInformation.minToneMapLuminance;
        float maxNits = cameraData.hdrDisplayInformation.maxToneMapLuminance;
        float paperWhite = cameraData.hdrDisplayInformation.paperWhiteNits;
    
        if (tonemapping != null)
        {
            // Tone mapping post process can override the luminance retrieved from the display
            if (!tonemapping.detectPaperWhite.value)
            {
                paperWhite = tonemapping.paperWhite.value;
            }
            if (!tonemapping.detectBrightnessLimits.value)
            {
                minNits = tonemapping.minNits.value;
                maxNits = tonemapping.maxNits.value;
            }
        }
    }
    

  7. Set the luminance properties of the material with the luminance data from the display and tonemapping.
    
        if (cameraData.isHDROutputActive && cameraData.postProcessEnabled)
    {
        var tonemapping = VolumeManager.instance.stack.GetComponent<Tonemapping>();
    
        // Get luminance information from the display, these define the dynamic range of the display.
        float minNits = cameraData.hdrDisplayInformation.minToneMapLuminance;
        float maxNits = cameraData.hdrDisplayInformation.maxToneMapLuminance;
        float paperWhite = cameraData.hdrDisplayInformation.paperWhiteNits;
    
        if (tonemapping != null)
        {
            // Tone mapping post process can override the luminance retrieved from the display
            if (!tonemapping.detectPaperWhite.value)
            {
                paperWhite = tonemapping.paperWhite.value;
            }
            if (!tonemapping.detectBrightnessLimits.value)
            {
                minNits = tonemapping.minNits.value;
                maxNits = tonemapping.maxNits.value;
            }
        }
    
        // Pass luminance data to the material, use these to interpret the range of values the
        // input will be in.
        material.SetFloat("_MinNits", minNits);
        material.SetFloat("_MaxNits", maxNits);
        material.SetFloat("_PaperWhite", paperWhite);
    }
    

  8. Retrieve the color gamut of the current color space and pass it to the material.
    
        // Pass luminance data to the material, use these to interpret the range of values the
    // input will be in.
    material.SetFloat("_MinNits", minNits);
    material.SetFloat("_MaxNits", maxNits);
    material.SetFloat("_PaperWhite", paperWhite);
    
    // Pass the color gamut data to the material (colorspace and transfer function).
    HDROutputUtils.GetColorSpaceForGamut(cameraData.hdrDisplayColorGamut, out int colorspaceValue);
    material.SetInteger("_HDRColorspace", colorspaceValue);
    

  9. Enable the HDR Output shader keywords.
    
        // Pass the color gamut data to the material (colorspace and transfer function).
    HDROutputUtils.GetColorSpaceForGamut(cameraData.hdrDisplayColorGamut, out int colorspaceValue);
    material.SetInteger("_HDRColorspace", colorspaceValue);
    
    // Enable HDR shader keywords
    material.EnableKeyword(HDROutputUtils.ShaderKeywords.HDR_INPUT);
    

  10. Call the SetupHDROutput method in your Execute() function to ensure that HDR Output is accounted for whenever this Scriptable Render Pass is in use.

## Complete Script Example

The following is the complete code from the example:

    
    
    class CustomFullScreenRenderPass : ScriptableRenderPass
    {
        // Leave your existing Render Pass code here
    
        static void SetupHDROutput(ref CameraData cameraData, Material material)
        {
            // If post processing is enabled, color grading has already applied tone mapping
            // As a result the input here will be in the display colorspace (Rec2020, P3, etc) and in nits
            if (cameraData.isHDROutputActive && cameraData.postProcessEnabled)
            {
                var tonemapping = VolumeManager.instance.stack.GetComponent<Tonemapping>();
    
                // Get luminance information from the display, these define the dynamic range of the display.
                float minNits = cameraData.hdrDisplayInformation.minToneMapLuminance;
                float maxNits = cameraData.hdrDisplayInformation.maxToneMapLuminance;
                float paperWhite = cameraData.hdrDisplayInformation.paperWhiteNits;
    
                if (tonemapping != null)
                {
                    // Tone mapping post process can override the luminance retrieved from the display
                    if (!tonemapping.detectPaperWhite.value)
                    {
                        paperWhite = tonemapping.paperWhite.value;
                    }
                    if (!tonemapping.detectBrightnessLimits.value)
                    {
                        minNits = tonemapping.minNits.value;
                        maxNits = tonemapping.maxNits.value;
                    }
                }
    
                // Pass luminance data to the material, use these to interpret the range of values the
                // input will be in.
                material.SetFloat("_MinNits", minNits);
                material.SetFloat("_MaxNits", maxNits);
                material.SetFloat("_PaperWhite", paperWhite);
    
                // Pass the color gamut data to the material (colorspace and transfer function).
                HDROutputUtils.GetColorSpaceForGamut(cameraData.hdrDisplayColorGamut, out int colorspaceValue);
                material.SetInteger("_HDRColorspace", colorspaceValue);
    
                // Enable HDR shader keywords
                material.EnableKeyword(HDROutputUtils.ShaderKeywords.HDR_INPUT);
            }
            else
            {
                // If HDR output is disabled, disable HDR output-related keywords
                // If post processing is disabled, the final pass will do the color conversion so there is
                // no need to account for HDR Output
                material.DisableKeyword(HDROutputUtils.ShaderKeywords.HDR_INPUT);
            }
        }
    }
    

[](../../urp/post-processing/hdr-output-implement-custom-overlay.html)

Implement an HDR Output compatible custom overlay in URP

[](../../graphics-performance-profiling.html)

Graphics performance and profiling

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://learn.unity.com/)[Community
Answers](https://answers.unity3d.com)[Knowledge
Base](https://support.unity3d.com/hc/en-
us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-
store)[Terms of
use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy
Policy](https://unity.com/legal/privacy-
policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share
My Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

